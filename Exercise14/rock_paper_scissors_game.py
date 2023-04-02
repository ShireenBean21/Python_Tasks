import random

while True:
    print("Welcome to the Rock Paper Scissors Game!")
    print("Rules: Rock breaks scissors, paper covers rock and scissors cuts paper\nCan you beat the Computer?\n")
    num_rounds = int(input("How many rounds would you like to play? "))
    player_score = 0
    computer_score = 0

    for i in range(num_rounds):
        print(f"Round {i+1}")
        player_choice = input("Choose (R)ock, (P)aper or (S)cissors: ").lower()

        if player_choice == 'r':
            player = "rock"
        elif player_choice == 'p':
            player = "paper"
        elif player_choice == 's':
            player = "scissors"
        else:
            print("Invalid input! Please choose again.")
            continue

        computer_num = random.randint(0, 2)
        if computer_num == 0:
            computer = "rock"
        elif computer_num == 1:
            computer = "paper"
        else:
            computer = "scissors"

        print(f"\nYou chose {player}, Computer chose {computer}.\n")

        if player == computer:
            print(f"You both chose {player}. It's a tie!")
        elif player == "rock":
            if computer == "scissors":
                print("Rock breaks Scissors. You win!")
                player_score += 1
            else:
                print("Paper covers Rock. Computer wins!")
                computer_score += 1
        elif player == "paper":
            if computer == "scissors":
                print("Scissors cuts Paper. Computer wins!")
                computer_score += 1
            else:
                print("Paper covers Rock. You win!")
                player_score += 1
        elif player == "scissors":
            if computer == "rock":
                print("Rock breaks Scissors. Computer wins!")
                computer_score += 1
            else:
                print("Scissors cuts Paper. You win!")
                player_score += 1

    print("Game Over!")
    print(f"You won {player_score} round(s) and the computer won {computer_score} round(s).")
    if player_score > computer_score:
        print("Congratulations! You won the game!")
    elif player_score < computer_score:
        print("Sorry, you lost the game.")
    else:
        print("The game ended in a tie.")

    new_game = input("Thanks for playing!\nDo you want to play again? (Y/N): ")
    if new_game.lower() != "y":
        break
