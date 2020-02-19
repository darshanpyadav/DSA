from pythonds.basic import Stack


def base_conversion(base, number):
    s = Stack()
    while number > 0:
        s.push(number % base)
        number = number // base
    return s


if __name__ == "__main__":
    a = base_conversion(2, 233)

    while not a.isEmpty():
        print(a.pop(), end="")
