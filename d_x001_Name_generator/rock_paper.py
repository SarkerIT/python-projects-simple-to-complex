from random import randint


comp_choice = randint(0, 2)
print(" Type: \n0 for Rock, \n1 for Paper, \n2 for Scissors\n")
your_choice = int(input("Your choice: "))
print(f"Computer's choice= {comp_choice}")

if your_choice == 0 and comp_choice == 1:
    print(f"\nYour choice is Rock and computer's choice is Paper.")
    print("Computer won!")
elif your_choice == 0 and comp_choice == 2:
    print(f"\nYour choice is Rock and computer's choice is Scissors.")
    print("You won!")
elif your_choice == 1 and comp_choice == 0:
    print(f"\nYour choice is Paper and computer's choice is Rock.")
    print("You won!")
elif your_choice == 1 and comp_choice == 2:
    print(f"\nYour choice is Paper and computer's choice is Scissors.")
    print("Computer won!")
elif your_choice == 2 and comp_choice == 0:
    print(f"\nYour choice is Scissors and computer's choice is Rock.")
    print("Computer won!")
elif your_choice == 2 and comp_choice == 1:
    print(f"\nYour choice is Scissors and computer's choice is paper.")
    print("You won!")
elif your_choice < 0 or your_choice > 2:
    print("\nYour choice is invalid!")
    print("Computer won!")
else:
    print("There is a tie!")
