# TODO: Преобразовать код в стиль ООП

example = '2 / 4'
operations = '+-*/'

left_operand, operator, right_operand = example.split()

left_operand = int(left_operand)
right_operand = int(right_operand)

if operator not in operations:
    print('Операция не поддерживается...')
elif operator == '+':
    print(left_operand + right_operand)

elif operator == '/':
    if right_operand == 0:
        print('Деление на ноль нельзя!')
    else:
        print(left_operand / right_operand)
