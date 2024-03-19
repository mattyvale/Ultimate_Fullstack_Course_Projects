import random

while True:
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    user_input = input("Make your choice: Rock, Paper or Scissors?: ").lower()

    if user_input == computer_choice:
        print(f"You both chose {computer_choice}. It's a draw!")
        continue
    elif user_input == 'rock':
        if computer_choice == 'scissors':
            print(f"You chose {user_input} and the computer chose {computer_choice}. You win!")
            break
        else:
            print(f"You chose {user_input} and the computer chose {computer_choice}. You lose!")
            continue
    elif user_input == 'paper':
        if computer_choice == 'rock':
            print(f"You chose {user_input} and the computer chose {computer_choice}. You win!")
            break
        else:
            print(f"You chose {user_input} and the computer chose {computer_choice}. You lose!")
            continue
    elif user_input == 'scissors':
        if computer_choice == 'paper':
            print(f"You chose {user_input} and the computer chose {computer_choice}. You win!")
            break
        else:
            print(f"You chose {user_input} and the computer chose {computer_choice}. You lose!")
            continue
    else:
        print(f"Invalid choice! Please enter a valid choice")
        continue
