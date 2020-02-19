from pythonds.basic import Stack


def dec(fun):
    def check_params(s):
        if not s:
            raise Exception("Please provide input")
        return fun(s)
    return check_params


@dec
def balance_parentheses(string):
    stack = Stack()

    for i in string:
        if i == "(":
            stack.push(i)
        elif i == ")":
            stack.pop()
        else:
            continue

    return stack.isEmpty()


if __name__ == "__main__":
    print("Stack is balanced: " + str(balance_parentheses("(()()()())")))
