# Function to perform calculation
def calculate():
    # Prompt user to input two numbers and an operation
    number_1 = int(input("Enter your first number: "))
    number_2 = int(input("Enter your second number: "))
    operation = input("Please type in the math operation you would like to complete:\n+ for addition\n- for subtraction\n* for multiplication\n/ for division\n")

    # Perform calculation based on user's choice
    if operation == '+':
        print(f"{number_1} + {number_2} = {number_1 + number_2}")
    elif operation == '-':
        print(f"{number_1} - {number_2} = {number_1 - number_2}")
    elif operation == '*':
        print(f"{number_1} * {number_2} = {number_1 * number_2}")
    elif operation == '/':
        print(f"{number_1} / {number_2} = {number_1 / number_2}")
    else:
        print("You have not typed a valid operator, please run the program again.")

    # Prompt user to calculate again
    calc_again = input("Do you want to calculate again?\nPlease type Y for YES or N for NO.\n")

    # If user types Y, run the calculate() function again
    if calc_again.upper() == 'Y':
        calculate()
    # If user types N, say good-bye to the user and end the program
    elif calc_again.upper() == 'N':
        print("See you later.")
    else:
        # If user types another key, run the function again
        again()

# Call calculate() outside of the function
calculate()