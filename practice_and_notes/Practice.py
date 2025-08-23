import psutil
import subprocess
import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from datetime import datetime

def generate_cpu_report():
    """Gather CPU stats using psutil."""
    cpu_cores = psutil.cpu_count(logical=False)
    cpu_threads = psutil.cpu_count(logical=True)
    cpu_percent_per_core = psutil.cpu_percent(interval=1, percpu=True)
    cpu_percent_total = sum(cpu_percent_per_core) / len(cpu_percent_per_core)

    raw_report = f"""
    System CPU Report:

    - CPU cores: {cpu_cores}
    - CPU threads: {cpu_threads}
    - Total CPU usage: {cpu_percent_total:.1f}%
    - Per-core usage: {', '.join([f'Core {i}: {p}%' for i, p in enumerate(cpu_percent_per_core)])}
    """
    return raw_report

def query_ollama(raw_report):
    """Send the CPU report to Ollama and get a plain-English explanation."""
    prompt = f"""
    You are an IT consultant. Rewrite this CPU report in plain English for a non-technical client.
    Explain why some cores are at high usage (like 90%) while others are low (1-10%).
    Give a clear explanation of what this means and include recommendations if necessary.

    {raw_report}
    """

    ollama_path = "/usr/local/bin/ollama"  # adjust if needed
    try:
        result = subprocess.run(
            [ollama_path, "run", "llama3", prompt],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return f"Ollama error: {e.stderr.strip() if e.stderr else str(e)}"

def save_pdf(client_text, raw_report):
    """Save the Ollama explanation (and raw stats) as a PDF on the Desktop."""
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    pdf_path = os.path.join(desktop_path, "CPU_Report.pdf")

    c = canvas.Canvas(pdf_path, pagesize=letter)
    width, height = letter

    # Title
    c.setFont("Helvetica-Bold", 16)
    c.drawString(1 * inch, height - 1 * inch, "Client-Friendly CPU Report")

    # Date
    c.setFont("Helvetica", 10)
    c.drawString(1 * inch, height - 1.2 * inch, f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    # Explanation text
    c.setFont("Helvetica", 11)
    y = height - 1.6 * inch
    for line in client_text.splitlines():
        for chunk in [line[i:i+90] for i in range(0, len(line), 90)]:
            c.drawString(1 * inch, y, chunk)
            y -= 14
            if y < 1 * inch:
                c.showPage()
                c.setFont("Helvetica", 11)
                y = height - 1 * inch
        y -= 8

    # Add raw stats on a new page
    c.showPage()
    c.setFont("Helvetica-Bold", 14)
    c.drawString(1 * inch, height - 1 * inch, "Technical System Stats")
    c.setFont("Helvetica", 11)
    y = height - 1.4 * inch
    for line in raw_report.splitlines():
        c.drawString(1 * inch, y, line.strip())
        y -= 14
        if y < 1 * inch:
            c.showPage()
            c.setFont("Helvetica", 11)
            y = height - 1 * inch

    c.save()
    return pdf_path

def main():
    raw_report = generate_cpu_report()
    client_text = query_ollama(raw_report)
    pdf_path = save_pdf(client_text, raw_report)
    print(f"\n✅ PDF saved to: {pdf_path}")

if __name__ == "__main__":
    main()