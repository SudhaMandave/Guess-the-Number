# Number Guessing Game

This is a simple number guessing game written in Python. The game generates a random number between 1 and 100, and the player has to guess the number. The game provides feedback on whether the guess is too high or too low and keeps track of the number of guesses.

## How to Play

1. Run the script.
2. The game will prompt you to guess a number between 1 and 100 or quit the game by entering 'Q'.
3. Enter your guess and press Enter.
4. The game will tell you if your guess is too high, too low, or correct.
5. If your guess is correct, the game will display the number of guesses you made and end the game.
6. If you want to quit the game at any time, enter 'Q'.

## Code Explanation

```python
import random   # Import the random module to generate random numbers

# Generate a random number between 1 and 100
randomNum = random.randint(1, 100)

# Initialize a counter variable to keep track of the number of guesses
guess_count = 0

# Start an infinite loop to allow repeated guessing
while True:
    # Prompt the user to guess the number or quit the game
    userChoiceNum = input("Guess the number OR Quit(Q): ")
    # Check if the user wants to quit the game
    if userChoiceNum == "Q":
        break

    try:
        userChoiceNum = int(userChoiceNum)
    except ValueError:
        # Handle the case where the user input is not a valid integer
        print("Please enter a valid number or 'Q' to quit.")
        continue  # Continue the loop to prompt the user again

    # Increment the guess counter
    guess_count += 1

    # Check if the user's guess is correct
    if userChoiceNum == randomNum:
        print("Success: Correct Guess!!")
        break
    elif userChoiceNum < randomNum:
        print("Your number was too small. Take a bigger guess...")
    else:
        print("Your number was too big. Take a smaller guess..")

# Print the number of guesses
print("Number of Guesses:", guess_count)

# Print a message indicating the end of the game
print("**********GAME OVER**********")
```

## Requirements

- Python 3.x

## Running the Game

1. Make sure you have Python 3.x installed on your machine.
2. Save the script to a file, for example, `number_guessing_game.py`.
3. Open a terminal or command prompt and navigate to the directory where the script is saved.
4. Run the script using the command: `python number_guessing_game.py`.

Enjoy the game!
