import random

# Function to determine the winner
def determine_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (player == "rock" and computer == "scissors") or \
         (player == "scissors" and computer == "paper") or \
         (player == "paper" and computer == "rock"):
        return "You win!"
    else:
        return "Computer wins!"

# Main game function
def rock_paper_scissors():
    choices = ["rock", "paper", "scissors"]
    player_score = 0
    computer_score = 0
    rounds = int(input("How many rounds do you want to play? "))

    for _ in range(rounds):
        # Get player's choice
        player_choice = input("Enter rock, paper, or scissors: ").lower()
        while player_choice not in choices:
            player_choice = input("Invalid choice. Please enter rock, paper, or scissors: ").lower()

        # Computer's random choice
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")

        # Determine and print the winner
        result = determine_winner(player_choice, computer_choice)
        print(result)

        # Update scores
        if "You win" in result:
            player_score += 1
        elif "Computer wins" in result:
            computer_score += 1

        print(f"Score: You {player_score} - {computer_score} Computer\n")

    # Final result after all rounds
    if player_score > computer_score:
        print("Congratulations! You won the game!")
    elif player_score < computer_score:
        print("Sorry, the computer won the game.")
    else:
        print("It's a tie game!")

# Start the game
rock_paper_scissors()
