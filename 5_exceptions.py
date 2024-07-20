while True:
    try:
        x = int(input("Please enter a number: "))
        print(f"Your number squared is: {x * x}")
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
