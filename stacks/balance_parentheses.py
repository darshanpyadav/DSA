from pythonds.basic import Stack


def dec(fun):
    def check_params(s):
        if not s:
            raise Exception("Please provide input")
        return fun(s)
    return check_params


@dec
def balance_parentheses(A):
    stack = []

    for i in A:
        if i == "(":
            stack.append(i)
        else:
            if len(stack) == 0:
                return 0
            stack.pop()

    return 1 if len(stack) == 0 else 0


if __name__ == "__main__":
    print("Stack is balanced: " + str(balance_parentheses("(()()()())")))
