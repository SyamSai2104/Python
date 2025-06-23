import random
options = ("rock","paper","scissors")
running = True

while running:

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice(rock,paper,scissors): ").lower()

    print(f"Player: {player}")
    print(f"computer: {computer}")
    if player == computer:
        print("Its a Tie")
    elif player == "rock" and computer == "scissors":
        print("You Won")
    elif player == "scissors" and computer == "paper":
        print("You Won")
    elif player == "paper" and computer =="rock":
        print("You Win")
    else:
        print("You Lose")

    if not input("Play again?: (y,n)").lower() =="y":
        running = False
print("Thanks for playing")