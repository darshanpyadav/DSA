from pythonds import Stack


def evaluate_postfix(postfix):
    # If operand, push into the stack
    # If operator, pop two operands, push the result into the stack
    # Pop result from stack
    stack = Stack()
    for i in postfix:
        if i.isalnum():
            stack.push(i)
        else:
            op2, op1 = str(stack.pop()), str(stack.pop())
            stack.push(eval(op1 + i + op2))
    return stack.pop()


if __name__ == "__main__":
    print(evaluate_postfix("78+32+/"))
