
import random

user_input = int(input("what is your choice, choose 0 for rock, 1 for paper and 2 for scisor."))

computer_choice = random.randint(0,2)
print("computer's choice is:", computer_choice)

if user_input not in [0,1,2]:
    print("you typed an invalid input, you lose")    
elif user_input == computer_choice:
    print("it's a draw")
elif (user_input == 0 and computer_choice == 2) or\
(user_input == 1 and computer_choice == 0) or\
(user_input == 2 and computer_choice == 1):
    print("you win")
else:
    print("you lose")