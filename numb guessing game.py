import random
def guessing_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed_correctly = False
    
    print("Welcome to the Number Guessing Game!")
    print("I have a number between 1 and 100 chosen. can you guess the number?")
    
    while not guessed_correctly:
        try:
            guess = int(input("Put a guess in: "))
            attempts += 1
            
            if guess < number_to_guess:
                print("To low! Try again.")
            elif guess > number_to_guess:
                print("To high! Try again.")
            else:
                guessed_correctly = True
                print(f"Congratualtions! You guessed the number {number_to_guess} in {attempts} guesses.")
        except ValueError:
            print("Error: give a valid number.")


if __name__ == "__main__":
    guessing_game()