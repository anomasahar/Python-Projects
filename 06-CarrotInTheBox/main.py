import random

print("Welcome To My Carrot In The Box Game")

p1Name = input('player 1, Enter your name: ')
p2Name = input('Player 2, Enter your name: ')
playerNames = p1Name[:11].center(11) + '    ' + p2Name[:11].center(11)

print('''HERE ARE TWO BOXES:
   __________     __________
  /         /|   /         /|
 +---------+ |  +---------+ |
 |   RED   | |  |   GOLD  | |
 |   BOX   | /  |   BOX   | /
 +---------+/   +---------+/''')

print(f'{p1Name}, you will get to look into your box.')
print(f'{p2Name}, close your eyes and don\'t look!!!')
input(f'When {p2Name} has closed their eyes, press Enter...')

if random.randint(1, 2) == 1:
    carrotInFirstBox = True
else:
    carrotInFirstBox = False

if carrotInFirstBox:
     print('''
    ___VV____
   |   VV    |
   |   VV    |
   |___||____|    __________
  /    ||   /|   /         /|
 +---------+ |  +---------+ |
 |   RED   | |  |   GOLD  | |
 |   BOX   | /  |   BOX   | /
 +---------+/   +---------+/
  (carrot!)''')
     print(playerNames)
else:
     print('''
    _________
   |         |
   |         |
   |_________|    __________
  /         /|   /         /|
 +---------+ |  +---------+ |
 |   RED   | |  |   GOLD  | |
 |   BOX   | /  |   BOX   | /
 +---------+/   +---------+/
 (no carrot!)''')
     print(playerNames)

input('Press Enter to continue...')

print('\n' * 10)  # Clear the screen by printing several newlines.
print(p1Name + ', tell ' + p2Name + ' to open their eyes.')
input('Press Enter to continue...')

print()
print(p1Name + ', say one of the following sentences to ' + p2Name + '.')
print('  1) There is a carrot in my box.')
print('  2) There is not a carrot in my box.')
print()
input('Then press Enter to continue...')

print()
while True:
    response = input(f'{p2Name}, do you want to swap boxes with {p1Name}? YES/NO: ').upper()
    if response.startswith('Y') or response.startswith('N'):
        break
    else:
        print(f'{p2Name}, please enter "YES" or "NO"')

firstBox = 'RED '
secondBox = 'GOLD'
if response.startswith('Y'):
    carrotInFirstBox = not carrotInFirstBox
    firstBox, secondBox = secondBox, firstBox

print('''HERE ARE THE TWO BOXES:
   __________     __________
  /         /|   /         /|
 +---------+ |  +---------+ |
 |   {}  | |  |   {}  | |
 |   BOX   | /  |   BOX   | /
 +---------+/   +---------+/'''.format(firstBox, secondBox))
print(playerNames)

input('Press Enter to reveal the winner...')
print()

if carrotInFirstBox:
    print('''
    ___VV____      _________
   |   VV    |    |         |
   |   VV    |    |         |
   |___||____|    |_________|
  /    ||   /|   /         /|
 +---------+ |  +---------+ |
 |   {}  | |  |   {}  | |
 |   BOX   | /  |   BOX   | /
 +---------+/   +---------+/'''.format(firstBox, secondBox))
 
else:
    print('''
    _________      ___VV____
   |         |    |   VV    |
   |         |    |   VV    |
   |_________|    |___||____|
  /         /|   /    ||   /|
 +---------+ |  +---------+ |
 |   {}  | |  |   {}  | |
 |   BOX   | /  |   BOX   | /
 +---------+/   +---------+/'''.format(firstBox, secondBox))
 
print(playerNames)

if carrotInFirstBox:
    print(p1Name + ' is the winner!')
else:
    print(p2Name + ' is the winner!')

print('Thanks for playing!')