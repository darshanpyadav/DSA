from deque.implementation import Deque


def palindrome(string):
    d = Deque()

    for i in string:
        d.addFront(i)

    while d.size() > 1:
        if d.removeFront() != d.removeRear():
            return False

    return True


print(palindrome("lsdkjfskf"))
print(palindrome("radar"))