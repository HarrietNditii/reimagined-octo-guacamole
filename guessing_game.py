import random

print("Welcome! This is a number guessing game! \nYou have 8 chances to guess the correct number!\nStart!")

guessed_number = random.randrange(100)
chances = 8
guess_counter = 0

while guess_counter < chances:
    guess_counter += 1
    my_guess = int(input("Enter your guess :"))

    if my_guess == guessed_number:
        print(f"The number is {guessed_number} and you found it at the {guess_counter} attempt")

        break
    elif guess_counter >= chances and my_guess != guessed_number:
   
        print(f'Oops sorry, The number is {guessed_number} better luck next time')

    elif my_guess > guessed_number:
        print('Your guess is higher ')

    elif my_guess < guessed_number:
        print('Your guess is lesser')