import random

user = input("Rock/Paper/Scissors or Q to Exit: ")

Rock = 1
Paper = 2
Scissors = 3

while user != 'Q':
    pc = random.randint(1, 3)
    if user == 'Rock':
        if pc == 1:
            print(f"Draw/Computer input: {pc}")
            user = input("Rock/Paper/Scissors or Q to Exit: ")
            continue
        elif pc == 2:
            print("Computer Win")
            break
        elif pc == 3:
            print("User Win")
            break
    elif user == 'Paper':
        if pc == 1:
            print("User Win")
            break
        elif pc == 2:
            print(f"Draw/Computer input: {pc}")
            user = input("Rock/Paper/Scissors or Q to Exit: ")
            continue
        elif pc == 3:
            print("Computer Win")
            break
    elif user == 'Scissors':
        if pc == 1:
            print("Computer Win")
            break
        elif pc == 2:
            print("User Win")
            break
        elif pc == 3:
            print(f"Draw/Computer input: {pc}")
            user = input("Rock/Paper/Scissors or Q to Exit: ")
            continue
    elif user != 'Rock' or user != 'Paper' or user != 'Scissors':
        print('Wrong Input, enter Rock/Paper/Scissors')
        continue
