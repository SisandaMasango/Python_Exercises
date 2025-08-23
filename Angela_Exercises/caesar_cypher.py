
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""

    for letter in original_text:
        if letter not in alphabet:
            output_text += letter
        else:
            if encode_or_decode == "decode":
                shift_amount *= -1
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {output_text}")

def questions():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
questions()

game_over = True
while game_over:
    question = input("Do you want to go again? ")
    if question == "yes":
        questions()
    elif question == "no":
        game_over = False
    else:
        print("Type Valid answer between yes and no.")
        questions()





