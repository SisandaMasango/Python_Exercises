import subprocess

# Tiny prompt to warm up the model
prompt = "1 + 1"

# Full path to Ollama
ollama_path = "/usr/local/bin/ollama"

# Run Ollama
result = subprocess.run(
    [ollama_path, "run", "llama2", prompt],
    capture_output=True,
    text=True
)

# Print result
if result.stderr:
    print("Ollama error:", result.stderr)
else:
    print("Warm-up output:", result.stdout)
