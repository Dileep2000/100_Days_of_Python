import random
if __name__ == "__main__":
    print("Welcome to ROCK PAPER SCISSORS GAME!")
    print("What do you choose? Type Rock, Paper or Scissors.")
    choice = input().lower()
    computer = random.choice(["Rock", "Paper", "Scissors"]).lower()
    print(f"Computer choose {computer}")
    if choice == computer:
        print("It's a Draw!")
    elif (choice == 'rock' and computer == 'scissors') or (choice == 'paper' and computer == 'rock') or (choice == 'scissors' and computer == 'paper'):
        print("You win!")
    else:
        print("You lose! Computer wins!")
