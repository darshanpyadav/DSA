from pythonds.basic import Stack
import unittest


def infix_to_postfix(exp):
    stack = Stack()
    result = ""
    priority = {'^': 3, '*': 2, '/': 2, '%': 2, '+': 1, '-': 1, '(': 0}

    for i in exp:
        if i.isalnum() or i.isalpha():
            result += i
        elif i == "(":
            stack.push(i)
        elif i == ")":
            while stack.peek() != "(":
                result += stack.pop()
            stack.pop()
        else:
            while not stack.isEmpty() and priority[stack.peek()] >= priority[i]:
                result += stack.pop()
            stack.push(i)

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
