import random
# Guess the Number Game
# This is a simple number guessing game where the player has to guess a randomly generated number.
def guess_the_number():
    number_to_guess = random.randint(1, 99)
    attempts = 0
    guessed_correctly = False

    print("Welcome to the Guess the Number Game!")
    print("I have selected a number between 1 and 99. Can you guess what it is?")

    while not guessed_correctly:
        try:
            player_guess = int(input("Enter your guess: "))
            attempts += 1

            if player_guess < number_to_guess:
                print("Too low! Try again.")
            elif player_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                guessed_correctly = True
                print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
        except ValueError:
            print("Please enter a valid integer.")

# Start the game
if __name__ == "__main__":
  guess_the_number()
