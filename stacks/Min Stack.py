'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) – Push element x onto stack.
pop() – Removes the element on top of the stack.
top() – Get the top element.
getMin() – Retrieve the minimum element in the stack.
Note that all the operations have to be constant time operations.

Questions to ask the interviewer :

Q: What should getMin() do on empty stack?
A: In this case, return -1.

Q: What should pop do on empty stack?
A: In this case, nothing.

Q: What should top() do on empty stack?
A: In this case, return -1
 NOTE : If you are using your own declared global variables, make sure to clear them out in the constructor.
'''


class MinStack:
    def __init__(self):
        self.items = []
        self.min = float('inf')

    # @param x, an integer
    def push(self, x):
        self.min = min(self.min, x)
        self.items.append((x, self.min))

    # @return nothing
    def pop(self):
        if not self.isEmpty():
            return self.items.pop()[0]

    # @return an integer
    def top(self):
        return -1 if self.isEmpty() else self.items[-1][0]

    # @return an integer
    def getMin(self):
        return -1 if self.isEmpty() else self.items[-1][1]

    def isEmpty(self):
        return len(self.items) == 0


s = MinStack()
print(s.pop())
s.push(644643544)
print(s.getMin())
print(s.top())
print(s.top())
print(s.top())
print(s.pop())
s.push(723943208)
print(s.pop())
s.push(909204)
print(s.getMin())
print(s.top())
print(s.getMin())
print(s.top())
s.push(481523691)
print(s.pop())
s.push(465865082)
print(s.top())
s.push(243519307)
print(s.pop())
print(s.top())
print(s.pop())
s.push(844871295)
print(s.getMin())
# p P 644643544 g t t t p P 723943208 p P 909204 g t g t P 481523691 p P 465865082 t P 243519307 p t p P 844871295 g
# 644643544 644643544 644643544 909204 909204 909204 909204 465865082 465865082 909204 573041392 909204