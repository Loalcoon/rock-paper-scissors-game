import random

options = {1: 'Rock', 2: 'Paper', 3:'Scissors'}

while True:
    user = input("Enter Rock/Paper/Scissors or Q to exit: ").capitalize()
    pc = random.randint(1, 3)

    if user == 'Q':
        print("Game exited")
        break

    if user not in options.values():
        print("Wrong input, please enter Rock/Paper/Scissors")
        break

    if user == options[pc]:
        print(f"Draw ; Computer Input: {options[pc]}")
        break
    elif ((user == "Rock" and options[pc] == "Scissors")
          or (user == "Paper" and options[pc] == "Rock")
          or (user == "Scissors" and options[pc] == "Paper")):
        print (f"User Win ; Computer Input: {options[pc]}")
        break
    else:
        print (f"Computer Win ; Input: {options[pc]}")
        break