import os
logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

print("Welcome to the Calculator APP!!")


def add(a, b):
    return a + b


def subtract(a, b):
    return a-b


def divide(a, b):
    return a/b


def multiply(a, b):
    return a*b


operations = {
    "+": add,
    "-": subtract,
    "/": divide,
    "*": multiply,
}

exit = False
while not exit:
    print(logo)
    num1 = float(input("What's the first number?: "))
    while True:
        operation = ""
        while True:
            operation = input(
                f"Pick and Operation from the options {' or '.join(operations.keys())} : ").lower()
            if operation not in operations.keys():
                print("Invalid operation. please try again.")
            else:
                break
        num2 = float(input("What's the second number?: "))
        answer = operations[operation](num1, num2)
        print(f"{num1} {operation} {num2} = {answer}")
        option = input("Would you like to use the current operation result as next input?\nType 'Y' to use the current operation result or 'C' or Continue with new operation or 'N' to exit: ").lower()
        if option == 'c':
            os.system("cls")
            break
        elif option == 'y':
            num1 = answer
        elif option == 'n':
            print("Thank you for using Calculator APP. See you again.")
            exit = True
            break
