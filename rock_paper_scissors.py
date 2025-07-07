import random

rock = '''
***ROCK***
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
***PAPER***
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
***SCISSORS***
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# # 0 wins against 2
# # 2 wins against 1
# # 1 wins against 0

list_of_symbols = [rock, paper, scissors]
computer = random.randint(0,2)
converted_computer = list_of_symbols[computer]
player = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for scissors. "))

result_message = ""
if player > 2 or player < 0:
   result_message = "Invalid input! You have lost!"
   converted_player = "No Move"
else: 
    converted_player = list_of_symbols[player]
    if player == 0 and computer == 2 or player == 2 and computer == 1 or player == 1 and computer == 0:
        result_message = "HOORAY!!!! YOU HAVE WON"
    # elif player == 0 and computer == 0 or player == 1 and computer == 1 or player == 2 and computer == 2:
    elif player == computer:
        result_message = "It is a draw, DO IT AGAIN"
    else:
        result_message = "WOMP, WOMP!!!! YOU HAVE LOST"
    

print("_________________________________________________________________________________________________")
print("PLAYER:")
print(converted_player)
print("_________________________________________________________________________________________________")
print("COMPUTER:")
# print(computer)
print(converted_computer)
print("_________________________________________________________________________________________________")
print(result_message)