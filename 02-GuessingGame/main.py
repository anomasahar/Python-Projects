import random

NUM_DIGITS = 2
MAX_GUESSES = 3

def getSecretNum():
    """Returns a string made up of NUM_DIGITS unique random digits."""
    numbers = list('0123456789')
    random.shuffle(numbers)

    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum

def getClues(guess, secretNum):
    """Returns a string with the pico, fermi, bagels clues for a guess
    and secret number pair."""
    if guess == secretNum:
        return 'You got it!'

    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Fermi')
        elif guess[i] in secretNum:
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagels' 
    else:
        clues.sort()
        return ' '.join(clues)


def main():

  print(f'''
  Bagels, a deductive logic game.
  I am thinking of a {NUM_DIGITS}-digit number with no repeated digits.
  Try to guess what it is. Here are some clues:
  When I say:    That means:
    Pico         One digit is correct but in the wrong position.
    Fermi        One digit is correct and in the right position.
    Bagels       No digit is correct.
  ''')
  
  while True:
    secretNum = getSecretNum()
    print('I have thought up a number.')
    print(f''' You have {MAX_GUESSES} guesses to get it.''')

    numGuesses = 1
    while numGuesses <= MAX_GUESSES:
        guess = ''
        while len(guess) != NUM_DIGITS or not guess.isdecimal():
            print('Guess #{}: '.format(numGuesses))
            guess = input('> ')

        clues = getClues(guess, secretNum)
        print(clues)
        numGuesses += 1

        if guess == secretNum:
            break  # They're correct, so break out of this loop.
        if numGuesses > MAX_GUESSES:
            print('You ran out of guesses.')
            print('The answer was {}.'.format(secretNum))
    print('Do you want to play again? (yes or no)')
    if not input('> ').lower().startswith('y'):
        break

  print("Thanks for playing!")


main()