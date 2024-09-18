import random

def higher_lower_game():
    print("Welcome to the Higher/Lower Game!")

    # Input validation for lower bound
    while True:
        try:
            lower_bound = int(input("Enter the lower bound: "))
            upper_bound = int(input("Enter the upper bound: "))

            if lower_bound >= upper_bound:
                print("Lower bound must be less than the upper bound. Try again.")
            else:
                break
        except ValueError:
            print("Please enter valid numbers for the bounds.")

    # Generate a random number between lower and upper bounds
    random_number = random.randint(lower_bound, upper_bound)

    # Game loop
    while True:
        try:
            user_guess = int(input(f"Enter your guess between {lower_bound} and {upper_bound}: "))

            if user_guess < lower_bound or user_guess > upper_bound:
                print(f"Your guess should be between {lower_bound} and {upper_bound}. Try again.")
            elif user_guess < random_number:
                print("Too low! Try again.")
            elif user_guess > random_number:
                print("Too high! Try again.")
            else:
                print("Congratulations! You guessed the correct number!")
                break
        except ValueError:
            print("Please enter a valid number.")

# Run the game
higher_lower_game()

input("press enter to exit")
