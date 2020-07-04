import re

def compute(x, operator, y):
    x, y = int(x), int(y)
    if operator == '+':
        return x + y
    return x - y

def check_number_of_operations(operations):
    return len(operations) > 5

def check_for_chars(problem):
    problem = ''.join(problem)
    char_finder = re.compile(r'[a-zA-Z]')
    if len(char_finder.findall(problem)):
        return True
    return False

def check_operators(operator):
    return operator not in ['+', '-']

def check_numbers(x, y):
    return len(list(str(x))) > 4 or len(list(str(y))) > 4

def print_formatter(calcs, solve):
    first_line, second_line, third_line, fourth_line, = '', '', '', '',

    for calc in calcs:
        width = max(len(calc[0]), len(calc[2])) + 2
        space = f'{" " * 4}'

        first_line  += f'{calc[0]: >{width}}' + space
        second_line += f'{calc[1]}' + f'{calc[2]: >{width-1}}' + space
        third_line  += f'{"-" * width}' + space
        fourth_line += f'{calc[3]: >{width}}' + space

    if solve:
        return '\n'.join((first_line, second_line, third_line, fourth_line))
    return '\n'.join((first_line, second_line, third_line))

def arithmetic_arranger(operations, solve=False):
    if check_number_of_operations(operations):
        return 'Error: Too many problems.'

    calcs = []

    for operation in operations:
        problem = operation.split()

        if check_for_chars(problem):
            return 'Error: Numbers must only contain digits.'

        x = int(problem[0])
        operator = problem[1]
        y = int(problem[2])

        if check_operators(operator):
            return "Error: Operator must be '+' or '-'."

        if check_numbers(x, y):
            return 'Error: Numbers cannot be more than four digits.'

        result = compute(x, operator, y)
        calcs.append([str(x), operator, str(y), str(result)])
    
    return print_formatter(calcs, solve)

func = arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"])

print(func)