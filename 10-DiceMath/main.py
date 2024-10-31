import random
import time

DICE_WIDTH = 9
DICE_HEIGHT = 5
CANVAS_WIDTH = 79
CANVAS_HEIGHT = 24 - 3

QUIZ_DURATION = 30  # Duration of the game in seconds.
MIN_DICE = 2        # Minimum number of dice per round.
MAX_DICE = 6        # Maximum number of dice per round.

REWARD = 4          # Points awarded for each correct answer.
PENALTY = 1         # Points deducted for each incorrect answer.

# Ensure the maximum number of dice doesn't exceed what can fit on the canvas:
assert MAX_DICE <= 14

D1 = ([
    '+-------+',
    '|       |',
    '|   O   |',
    '|       |',
    '+-------+'
], 1)

D2a = ([
    '+-------+',
    '| O     |',
    '|       |',
    '|     O |',
    '+-------+'], 2)
 
D2b = ([
    '+-------+',
    '|     O |',
    '|       |',
    '| O     |',
    '+-------+'], 2)
 
D3a = ([
    '+-------+',
    '| O     |',
    '|   O   |',
    '|     O |',
    '+-------+'], 3)
 
D3b = ([
    '+-------+',
    '|     O |',
    '|   O   |',
    '| O     |',
    '+-------+'], 3)
 
D4 = ([
    '+-------+',
    '| O   O |',
    '|       |',
    '| O   O |',
    '+-------+'], 4)

D5 = ([
    '+-------+',
    '| O   O |',
    '|   O   |',
    '| O   O |',
    '+-------+'], 5)
 
D6a = ([
    '+-------+',
    '| O   O |',
    '| O   O |',
    '| O   O |',
    '+-------+'], 6)
 
D6b = ([
    '+-------+',
    '| O O O |',
    '|       |',
    '| O O O |',
    '+-------+'], 6)

ALL_DICE = [D1, D2a, D2b, D3a, D3b, D4, D5, D6a, D6b]

print('''Welcome To My MathDice Game

Add up the sides of all the dice displayed on the screen. You have
{} seconds to answer as many as possible. You get {} points for each
correct answer and lose {} point for each incorrect answer.
'''.format(QUIZ_DURATION, REWARD, PENALTY))
input('Press Enter to begin...')

correctAnswers = 0
incorrectAnswers = 0
startTime = time.time()

while time.time() < startTime + QUIZ_DURATION:
    sumAnswer = 0
    diceFaces = []
    for i in range(random.randint(MIN_DICE, MAX_DICE)):
        die = random.choice(ALL_DICE)
        diceFaces.append(die[0])  # The ASCII art representation of the die face.
        sumAnswer += die[1]       # The die's numerical value.

    topLeftDiceCorners = []

    for i in range(len(diceFaces)):
        while True:
            left = random.randint(0, CANVAS_WIDTH  - 1 - DICE_WIDTH)
            top  = random.randint(0, CANVAS_HEIGHT - 1 - DICE_HEIGHT)

            # Calculate the positions of the die's corners.
            topLeftX = left
            topLeftY = top
            topRightX = left + DICE_WIDTH
            topRightY = top
            bottomLeftX = left
            bottomLeftY = top + DICE_HEIGHT
            bottomRightX = left + DICE_WIDTH
            bottomRightY = top + DICE_HEIGHT

            # Check for overlaps with previously placed dice.
            overlaps = False
            for prevDieLeft, prevDieTop in topLeftDiceCorners:
                prevDieRight = prevDieLeft + DICE_WIDTH
                prevDieBottom = prevDieTop + DICE_HEIGHT

                # Check if any corner of the new die overlaps with previous dice.
                for cornerX, cornerY in (
                    (topLeftX, topLeftY),
                    (topRightX, topRightY),
                    (bottomLeftX, bottomLeftY),
                    (bottomRightX, bottomRightY)
                ):
                    if (prevDieLeft <= cornerX < prevDieRight and
                        prevDieTop <= cornerY < prevDieBottom):
                        overlaps = True
                        break  # No need to check other corners if overlap is found.
                if overlaps:
                    break  # Try a new position.

            if not overlaps:
                # The die does not overlap with any others, so place it.
                topLeftDiceCorners.append((left, top))
                break
    canvas = {}
    for i, (dieLeft, dieTop) in enumerate(topLeftDiceCorners):
        dieFace = diceFaces[i]
        for dx in range(DICE_WIDTH):
            for dy in range(DICE_HEIGHT):
                canvasX = dieLeft + dx
                canvasY = dieTop + dy
                # Note that in dieFace, the rows (dy) come before columns (dx).
                canvas[(canvasX, canvasY)] = dieFace[dy][dx]

    for cy in range(CANVAS_HEIGHT):
        for cx in range(CANVAS_WIDTH):
            print(canvas.get((cx, cy), ' '), end='')
        print()  # Move to the next line.

    response = input('Enter the sum: ').strip()
    if response.isdecimal() and int(response) == sumAnswer:
        correctAnswers += 1
    else:
        print('Incorrect, the answer is', sumAnswer)
        time.sleep(2)
        incorrectAnswers += 1

score = (correctAnswers * REWARD) - (incorrectAnswers * PENALTY)
print('Correct:  ', correctAnswers)
print('Incorrect:', incorrectAnswers)
print('Score:    ', score)


