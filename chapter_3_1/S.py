expression = input().split()

stack = []
for item in expression:
    if item.isdigit():
        stack.append(int(item))
    else:
        right_operand = stack.pop()
        left_operand = stack.pop()
        # right_operand = stack[-1]
        # left_operand = stack[-2]
        #
        # del stack[-1]
        # del stack[-2]
        if item == '+':
            stack.append(left_operand + right_operand)
        elif item == '-':
            stack.append(left_operand - right_operand)
        elif item == '*':
            stack.append(left_operand * right_operand)
    # if len(stack) == 1:
    #     print(stack[0])
    #     break
print(stack[0])
