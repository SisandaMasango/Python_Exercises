def simple_hash(text, modulus=1000000007):
    """A very simple hash function using modulo."""
    hash_value = 0
    for char in text:
        # Combine the current hash with the character's Unicode code point
        hash_value = (hash_value * 31 + ord(char)) % modulus
    return hash_value

# Test with some strings
print(simple_hash("hello"))  # Output a number between 0 and 1000000006
print(simple_hash("world"))
print(simple_hash("hello world"))
print(simple_hash("こんにちは"))  