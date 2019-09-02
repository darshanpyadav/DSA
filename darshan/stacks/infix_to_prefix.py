from darshan.stacks.infix_to_postfix import infix_to_postfix
import unittest


def infix_to_prefix(exp):
    exp = list(exp[::-1])
    for i in range(len(exp)):
        if exp[i] == "(":
            exp[i] = ")"
        if exp[i] == ")":
            exp[i] = "("
    return (infix_to_postfix("".join(exp)))[::-1]


class TestInfixToPrefix(unittest.TestCase):
    def test_expressions(self):
        expressions = {"(A+B)*(C+D)": "*+AB+CD", "A*B+C*D": "+*AB*CD"}
        results = [infix_to_prefix(expression) for expression in expressions]
        self.assertListEqual(results, list(expressions.values()))


if __name__ == "__main__":
    unittest.main()
