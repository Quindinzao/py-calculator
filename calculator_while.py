while True:
    num1 = input('Number 1: ')
    num2 = input('Number 2: ')
    operator = input('Operator (+ - * /): ')

    valid_numbers = None

    num1_float = 0
    num2_float = 0

    try:
        num1_float = float(num1)
        num2_float = float(num2)
        valid_numbers = True
    except Exception as error:
        valid_numbers = None

    if (valid_numbers is None):
        print('Invaid numbers')
        continue

    valid_operators = '+-*/'

    if (operator not in valid_operators):
        print('Invaid operator')
        continue

    if (operator == '+'):
        print(num1_float + num2_float)
    if (operator == '-'):
        print(num1_float - num2_float)
    if (operator == '*'):
        print(num1_float * num2_float)
    if (operator == '/'):
        print(num1_float / num2_float)

    exit = input('Are you wanna exit? (y/n)\n').lower().startswith('y')
    if (exit):
        break
