import re


def isNumber(A):
    num = '-?(\d*\.)?\d+'
    reg = '^\s*' + num + '(e-?\d+)?\s*$'
    if re.search(reg, A):
        return 1
    else:
        return 0
