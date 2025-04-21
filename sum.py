def main():
    print("This program adds two numbers.")

    # Get first number from user and convert to integer
    num1 = int(input("Enter the first number: "))

    # Get second number from user and convert to integer
    num2 = int(input("Enter the second number: "))

    # Calculate sum
    total = num1 + num2

    # Output result
    print("The total is " + str(total) + ".")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
