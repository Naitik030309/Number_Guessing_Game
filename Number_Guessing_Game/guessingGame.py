import random
print('Number Guessing Game')

randnum = random.randint(1,9)
chances = 0
print('Guess any number between 1 to 9!')

#While loop to count the number of chances
while chances < 5:

    guess = int(input('Enter your guessed number!'))

    # Compare the user entered number with the number to be guessed

    if guess == randnum:
        # If number entered by user is same as the generated
        # number by randint function then break from loop using loop
        # control statement "break"
        print('Congratulations! You guessed the number!')
        break

    elif guess > randnum:
        print('Your guess was too high! Guess a number lower than', guess)

    else:
        print('Your guess was too low! Guess a number higher than',guess)

        chances+=1

    # Check whether the user guessed the correct number
    if not chances < 5:
        print('You Lose! The number was',randnum)        