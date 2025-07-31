import random
stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list = ["cat", "vat", "dog"]
lives = 6
chosen_word = random.choice(word_list)
# print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []
guessed_letters = []



while not game_over:

    print(f"****************************<???>/{lives} LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()
    display = ""
    if guess not in guessed_letters:
        guessed_letters.append(guess)
        # print(guessed_letters)

        for letter in chosen_word:
            if letter == guess:
                display += letter
                correct_letters.append(guess)
            elif letter in correct_letters:
                display += letter
            else:
                display += "_"

        print("Word to guess: " + display)

        if guess not in chosen_word:
            print(f"You guessed {guess} and it is not in the chosen word, You lose a life")
            lives -= 1

            if lives == 0:
                game_over = True
                print(f"You were trying to guess {chosen_word}")
                print(f"***********************IT WAS <{chosen_word}>! YOU LOSE**********************")

        if "_" not in display :
            game_over = True
            print("****************************YOU WIN****************************")

    else:
        print(f" {guess } was already guessed, try another letter")

    
    print(stages[lives])
