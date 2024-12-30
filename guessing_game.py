# A program for guessing a game using the match case way.
import random

count = 0
play = "yes"
while play == "yes":

    secret_number = random.randint(1, 10)    
    guess = int(input("Guess a number between 1 and 10: "))
    
    match guess:
        case _ if guess == secret_number:
            print("Congratulations, you guessed it!")

            break

        case _ if guess > secret_number:
            print("Oops, your guess is a bit high. Try again!")
        case _ if guess < secret_number:
            print("Nope, your guess is a bit low. Give it another shot!")

    play = input("Play again? (yes/no): ").lower()
    count += 1
print(f"Thank you for playing, you played {count} time(s)")
