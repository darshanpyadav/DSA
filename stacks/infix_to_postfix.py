from pythonds.basic import Stack
import unittest


def infix_to_postfix(exp):
    stack = Stack()
    result = ""
    priority = {'^': 3, '*': 2, '/': 2, '%': 2, '+': 1, '-': 1, '(': 0}

    for i in exp:
        # if alnum, then add to the result string
        if i.isalnum():
            result += i
        # if (, then push it to the stack
        elif i == "(":
            stack.push(i)
        # if ) then, pop all the elements till you encounter (, including (
        elif i == ")":
            while stack.peek() != "(":
                result += stack.pop()
            stack.pop()
        # if it's an operator, pop until the rank of the op in stack is >= the current op
        else:
            while not stack.isEmpty() and priority[stack.peek()] >= priority[i]:
                result += stack.pop()
            stack.push(i)

    # pop all the remaining elements to result
    while not stack.isEmpty():
        result += stack.pop()

    return result


class TestInfixToPostfix(unittest.TestCase):
    def test_expressions(self):
        expressions = {"A+B*C+D": "ABC*+D+", "(A+B)*(C+D)": "AB+CD+*", "A*B+C*D": "AB*CD*+", "A+B+C+D": "AB+C+D+"}
        results = [infix_to_postfix(expression) for expression in expressions]
        self.assertListEqual(results, list(expressions.values()))


if __name__ == "__main__":
    unittest.main()
