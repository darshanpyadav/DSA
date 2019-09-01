from pythonds.basic import Stack


def balance_brackets(string):
    stack = Stack()
    open = "([{"
    close = ")]}"

    for i in string:
        if i in open:
            stack.push(i)
        else:
            if stack.isEmpty() or open.index(stack.peek()) != close.index(i):
                return False
            stack.pop()

    return stack.isEmpty()


if __name__ == "__main__":
    print("Stack is balanced: " + str(balance_brackets("[[{{(())}}]]")))
    print("Stack is balanced: " + str(balance_brackets("[{()]")))
