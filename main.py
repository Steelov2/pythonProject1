firstNumber = tuple([eval(val) for val in input("Please enter the first number (ex: 1/5): ").split('/')])
secondNumber = tuple([eval(val) for val in input("Please enter the second number (ex: 2/7): ").split('/')])


def multiply():
    print(int(firstNumber[0]) * int(secondNumber[0]), '/', int(firstNumber[1] * secondNumber[1]))


def divide():
    print(int(firstNumber[0]) * int(secondNumber[1]), '/', int(firstNumber[1] * secondNumber[0]))


def smallest():
    final_list = []
    line = input("Enter the fraction:")
    while line != '':
        final_list.append(tuple([eval(val) for val in input("Please enter the first number (ex: 1/5): ").split('/')]))
        line = input("Enter the fraction:")

    print(final_list)


smallest()

# while True:
#     a = input('Enter the command:')
#     if a == "again":
#         firstNumber = tuple([eval(val) for val in input("Please enter the first number (ex: 1/5): ").split('/')])
#         secondNumber = tuple([eval(val) for val in input("Please enter the second number (ex: 2/7): ").split('/')])
#         print(firstNumber)
