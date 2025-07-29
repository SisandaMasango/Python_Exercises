alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(direction):
    if direction == "decrypt":

        def decrypt(original_text, shift_amount):
            decrypt_text = ""
            for letter in original_text:
                shifted_position = alphabet.index(letter) - shift_amount
                decrypt_text += alphabet[shifted_position]
            print(f"Here is the encoded result: {decrypt_text}")
        decrypt(text, shift)

    elif direction == "encode":


        def encrypt(original_text, shift_amount):
            cipher_text = ""
            for letter in original_text:
                shifted_position = alphabet.index(letter) + shift_amount
                shifted_position %= len(alphabet)
                cipher_text += alphabet[shifted_position]
            print(f"Here is the encoded result: {cipher_text}")
        encrypt(text, shift)
    else:
        print("Try Again")
caesar(direction)



