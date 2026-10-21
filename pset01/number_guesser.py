import random

secret_number = random.randint(1, 100)
guess_count = 0
while True:
    guess = input("Guess a number between 1 and 100 (or type 'exit' to quit): ")
    if guess.lower() == 'exit':
        print("Thanks for playing!")
        break
    try:
        guess = int(guess)
        if guess < 1 or guess > 100:
            print("Please guess a number within the range of 1 to 100.")
            continue
    except ValueError:
        print("Please enter a valid integer.")
        continue

    guess_count += 1
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You've guessed the secret number:", secret_number)
        print("It took you", guess_count, "guesses.")
        break
