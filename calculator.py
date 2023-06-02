def initialize_calculator():
    operator = input('1. Adição\n2. Subtração\n3. Multiplicação\n4. Divisão\n5. Sair\n\nEscolha uma ação baseada nos números do menu: \n')
    if (operator == '1'):
        addition()
    elif (operator == '2'):
        subtraction()
    elif (operator == '3'):
        multiplication()
    elif (operator == '4'):
        division()
    elif (operator == '5'):
        exit()
    else:
        error('Unknown operator!')

def addition():
    num1 = numbers('Digite a primeira parcela: ', 'Invalid character')
    num2 = numbers('Digite a segunda parcela: ', 'Invalid character')
    print(f'\nA soma entre {num1} e {num2} é {num1 + num2}\n')
    initialize_calculator()

def subtraction():
    num1 = numbers('Digite o minuendo: ', 'Invalid character!')
    num2 = numbers('Digite o subtreaendo: ', 'Invalid character!')
    print(f'\nA subtração entre {num1} e {num2} é {num1 - num2}\n')
    initialize_calculator()

def multiplication():
    num1 = numbers('Digite o primeiro fator: ', 'Invalid character!')
    num2 = numbers('Digite o segundo fator: ', 'Invalid character!')
    print(f'\nA multiplicação entre {num1} e {num2} é {num1 * num2}\n')
    initialize_calculator()

def division():
    num1 = numbers('Digite o dividendo: ', 'Invalid character!')
    num2 = numbers('Digite o subtraendo: ', 'Invalid character!')
    if (num2 == 0):
        error('Não existe divisão por 0!')
    print(f'\nA divisão entre {num1} e {num2} é {num1 / num2}\n')
    initialize_calculator()

def numbers(text, message_error): 
    num = input(text)
    is_number_num = str.isnumeric(num)
    if (is_number_num == False):
        error(message_error)
    else:
        return float(num)

def error(message_error):
    print(f'\nError: {message_error}\n')
    initialize_calculator()

initialize_calculator()