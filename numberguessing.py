import random

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num,highest_num)
guesses = 0
is_running = True

#Displaying the title and number to choose from
print("Python Number Guessing Game")
print(f"Select number between {lowest_num} and {highest_num}")

#Asking for input,checking and comparing the input
while is_running:
    guess = input("Enter your guess: ")
    if guess.isdigit():
        guess = int(guess)
        guesses +=1 
        if guess<lowest_num or guess>highest_num:
           print(f"Please select number between {lowest_num} and {highest_num}")
        elif guess<answer:
            print("Too Low")
        elif guess>answer:
            print("Too High")
        else:
            print(f"Correct! The answer was {answer}")
            print(f"You took {guesses} guesses")
            is_running = False 
    else:
        print("Invalid number")
        print(f"Please select number between {lowest_num} and {highest_num}")