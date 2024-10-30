import math, sys

while True:  # Main program loop.
    print('Enter a positive whole number to factor (or QUIT):')
    response = input('> ')
    if response.upper() == 'QUIT':
        sys.exit()

    if not (response.isdecimal() and int(response) > 0):
        print('Invalid Response')
        continue
    number = int(response)

    factors = []

    # Find the factors of number:
    for i in range(1, int(math.sqrt(number)) + 1):
        if number % i == 0:  # If there's no remainder, it is a factor.
            factors.append(i)
            factors.append(number // i)
    
    # Convert to a set to get rid of duplicate factors:
    factors = list(set(factors))
    factors.sort()

    # Display the results:
    for i, factor in enumerate(factors):
        factors[i] = str(factor)
    print(', '.join(factors))

    if len(factors) == 2:
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is a composite number.")