# Calculator Assignment

def main():
    print("Welcome To My Calculator Project")
    x:int = int(input("Enter any value:"))
    y:int = int(input("Enter another value:"))
    print("Select operation:")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Power")
    print("6.Modulus")
    print("7.Floor")
    choice:int = int(input("Which Operation You Want To Perform?"))
    if choice == 1:
        sum = x+y
        print("First Number =" , x )
        print("Second Number =" , y )
        print("Result:",sum)
    elif choice == 2:
        sub = x-y
        print("First Number =" , x )
        print("Second Number =" , y )
        print("Result:",sub)
    elif choice == 3:
        mul = x*y
        print("First Number =" , x )
        print("Second Number =" , y )
        print("Result:",mul)
    elif choice == 4:
        div = x/y
        if y == 0:
            print("Error!")
        else:
            print("First Number =" , x )
            print("Second Number =" , y )
            print("Result:",div)
    elif choice == 5:
        pow = x**y
        print("First Number =" , x )
        print("Second Number =" , y )
        print("Result:",pow)
    elif choice == 6:
        mod = x%y
        print("First Number =" , x )
        print("Second Number =" , y )
        print("Result:",mod)
    elif choice == 7:
        floor = x//y
        print("First Number =" , x )
        print("Second Number =" , y )
        print("Result:",floor)
    else:
        print("Invalid Choice")
    

main()
