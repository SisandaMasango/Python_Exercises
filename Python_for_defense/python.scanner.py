import socket
from ipaddress import ip_network
from concurrent.futures import ThreadPoolExecutor, as_completed
import subprocess
import json

def is_open(ip, port, timeout=0.5):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(timeout)
        try:
            s.connect((str(ip), port))
            return True
        except:
            return False

def scan_host(ip, ports):
    open_ports = []
    for port in ports:
        if is_open(ip, port):
            open_ports.append(port)
    return ip, open_ports

def scan_network(network_cidr, ports, max_workers=100):
    net = ip_network(network_cidr)
    results = {}

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(scan_host, ip, ports): ip for ip in net.hosts()}

        for future in as_completed(futures):
            ip, open_ports = future.result()
            if open_ports:
                results[str(ip)] = open_ports

    return results

def ask_ollama(conversation, model="llama3"):
    """
    Sends the entire conversation history to Ollama.
    `conversation` is a list of dicts: {"role": "user"/"assistant", "content": "..."}
    """
    # Build a chat-style prompt for Ollama
    prompt_text = ""
    for turn in conversation:
        role = "User" if turn["role"] == "user" else "Assistant"
        prompt_text += f"{role}: {turn['content']}\n"

    process = subprocess.Popen(
        ["ollama", "run", model],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    output, error = process.communicate(prompt_text)
    if error:
        print("Error from Ollama:", error)
    return output.strip()

def main():
    network = input("Enter network to scan (e.g. 192.168.0.0/24): ")
    ports_input = input("Enter ports to scan, separated by commas (e.g. 21,22,80,443): ")

    ports = [int(p.strip()) for p in ports_input.split(",")]

    print(f"Scanning network {network} on ports {ports}...")
    results = scan_network(network, ports)

    if results:
        print("\nScan results:")
        for ip, open_ports in results.items():
            print(f"IP {ip} has open ports: {open_ports}")

        # Start conversation history
        conversation = []
        initial_prompt = f"""
You are a professional network security analyst. Here are the network scan results:
{json.dumps(results, indent=2)}

Write a clear, professional report explaining:
1. Which hosts were found online.
2. Which ports are open on each host.
3. The possible risks of these open ports.
4. Recommendations for securing the network.

At the end, say:
"Do you have any more questions? Type 'done' when you are satisfied with the report."
        """
        conversation.append({"role": "user", "content": initial_prompt})

        # Get first report from Ollama
        report = ask_ollama(conversation)
        conversation.append({"role": "assistant", "content": report})

        print("\n--- Security Report ---\n")
        print(report)

        # Interactive Q&A with memory
        while True:
            follow_up = input("\nYour question (or type 'done'): ").strip()
            if follow_up.lower() == "done":
                print("Thank you. Session ended.")
                break

            conversation.append({"role": "user", "content": follow_up})
            answer = ask_ollama(conversation)
            conversation.append({"role": "assistant", "content": answer})

            print("\n--- Response ---\n")
            print(answer)

    else:
        print("No open ports found.")

if __name__ == "__main__":
    main()
