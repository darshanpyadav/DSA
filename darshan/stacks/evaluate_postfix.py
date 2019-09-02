from pythonds import Stack


def evaluate_postfix(postfix):
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
