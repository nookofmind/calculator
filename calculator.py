# Imports and external libraries
import re
from datetime import datetime


# Functions' definitions
def takeInput():
    userTextInput = input("Enter equation\n")
    # Test function
    print("Function takeInput was executed. Output was", userTextInput)
    # End function
    return userTextInput


def calculate_userTextInput(userInput):
    result = eval(userInput)
    # Test function
    print("Function calculate_userTextInput was executed. Input was", userInput, "Output was", result)
    # Show result
    print(result)

    # Comment result
    if result < 0:
        print('Your result is negative')
    elif result > 0:
        print('Your result is positive')
    else:
        print('Your result is equal to zero')

    # Date
    dt = datetime.now()
    dotindex = str(dt).rfind(".")
    print("Date and time is:", str(dt)[: dotindex])

    # Timestamp
    ts = datetime.timestamp(dt)
    print("Timestamp is:", ts)

    # End function
    return result

# Function definition - read external file
def search_str(file_path, word):

    # Date - to look for weekends
    dt = datetime.now()

    # Read the file
    with open(file_path, 'r') as file:
        content = file.read()

        # Show weekday and day name
        print('Weekday is:', dt.isoweekday())
        print('day Name:', dt.strftime('%A\n'))

        # Define the version of the program
        if word in content:
            print('Welcome to the premium version - you can make calculations everyday!\n')
        else:
            print('Welcome to the demo version - you can make calculations only on business days.\n')

            # Stop the calculator for demo users during the weekend
            if dt.isoweekday() in range(6, 7):
                print("Calculating during the weekend is only for premium users")
                quit()

# Run the function - read external file
search_str(r'C:\Users\MPC\PycharmProjects\pythonProject\license.txt', 'premium_version')

# Instruction section
print("Calculator has started")
print("Type quit to exit\n")

# Quit
runCalculator = True

while runCalculator:
    functionResult = takeInput()

    if functionResult == 'quit':
        print("See you next time!")
        runCalculator = False

    # Validation
    else:
        functionResult = re.sub('[a-zA-Z!@#$^&=%_\",?/.:;{}\\\()" "]', '', functionResult)
        if functionResult == '':
            print("You can use only numbers")

        # Calculate
        else:
            calculate_userTextInput(functionResult)
