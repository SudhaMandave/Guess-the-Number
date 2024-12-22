import random   #import the random module to generate random numbers

# Generate a random number between 1 and 100
randomNum = random.randint(1, 100)

# Initialize a counter variable to keeo track of the number of guesses
guess_count = 0

# Start an infinite loop to allow repeated guessing 
while True:
  # Prompt the user to guess the number or quit the game
  userChoiceNum = input("Guess the number OR Quit(Q): ")
  # Check if the user wants to quit the game
  if (userChoiceNum == "Q"):
    break 

  try:
    userChoiceNum = int(userChoiceNum)
  except ValueError:
    # Handle the case where the user input is not a valid integer
    print("Please enter a valid number or 'Q' to quit.")
    continue  #Continue the loop to prompt the user again
  
  # Increment the guess counter
  guess_count += 1

  # Check if the user's guess
  if (userChoiceNum == randomNum):
    print("Sucess : Correct Guess!!")
    break
  elif (userChoiceNum < randomNum):
    print("Your number was too small. Take a bigger guess...")
  else:
    print("Your number was too big. Take a smaller guess..")

# Print number of guess number
print("Number of Guess", guess_count)

# Print a message indicating the end of the game
print("**********GAME OVER**********")