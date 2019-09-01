from pythonds.basic import Stack


def balance_parentheses(string):
    stack = Stack()

    for i in string:
        if i == "(":
            stack.push(i)
        else:
            if stack.isEmpty():
                return False
            stack.pop()

    return stack.isEmpty()


if __name__ == "__main__":
    print("Stack is balanced: " + str(balance_parentheses("(()()()())")))
