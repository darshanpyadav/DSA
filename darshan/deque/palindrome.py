from darshan.deque.implementation import Deque


def palindrom(string):
    d = Deque()

    for i in string:
        d.addFront(i)

    while d.size() > 1:
        if d.removeFront() != d.removeRear():
            return False

    return True


print(palindrom("lsdkjfskf"))
print(palindrom("radar"))