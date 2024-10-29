bitmap = """
....................................................................
   **************   *  *** **  *      ******************************
  ********************* ** ** *    ******************************
 **      *****************       ******************************
          *************          **  * **** ** **************
           *********            *** *** *   **** ** * *********
            ********           ********      * *** *** *******
   *        * **** ***         ********         ** ** ** **
               **** *         ********
                 ****         **** ***           * ***
                 **          **** **             *  **
..............................................................
"""

message = input("Enter the message to display with the bitmap:")

# splitlines() method splits the multi-line string into individual lines, 
# which are then processed one by one in the loop

# Loop over each line in the bitmap:
for line in bitmap.splitlines():
    # Loop over each character in the line:
    for i, bit in enumerate(line): 
        if bit == ' ':
            # Print an empty space since there's a space in the bitmap:
            print(' ', end='') 
        else:
            # Print a character from the message:
            print(message[i % len(message)], end='') 
    print() # Print a newline