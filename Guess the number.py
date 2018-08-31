import random
guesses = 0
number = random.randint(1, 10)
print('Guess a number between 1 and 10.')
while guesses < 5:
    print('Take a guess')
    entry = input()
    guess = int(entry)

    guesses = guesses+ 1

    if guess < number:
        print('too low')

    elif guess > number:
        print('too high')

    else :
     break


if guess == number:
     guesses = str(guesses)
     print('correct! you guessed the number in '+guesses+' guesses')

if guess != number:
    number = str( number)
    print(' Sorry, you used all of your chances. The number is '+ number)
