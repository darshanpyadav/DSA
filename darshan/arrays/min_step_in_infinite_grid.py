# *****************************************************************************
# Author            : darshanp
# Date              : 14/09/19
# Last modified by  : darshanp
# Version           : 1.0
# Description       : Let-s-do-it
# *****************************************************************************

# Problem
'''
You are in an infinite 2D grid where you can move in any of the 8 directions :

(x,y) to
(x+1, y),
(x - 1, y),
(x, y+1),
(x, y-1),
(x-1, y-1),
(x+1,y+1),
(x-1,y+1),
(x+1,y-1)
You are given a sequence of points and the order in which you need to cover the points. Give the minimum number of steps
in which you can achieve it. You start from the first point.
'''

# First number is length
# Input
# a = 3 1 3 6
# b = 3 1 3 6

# So input co-ordinates is [(1,1), (3,3), (6,6)]

# Output
# 5

# (1,1) to (3,3) is 2
# (3,3) to (6,6) is 3


def min_steps(a, b):
    # just get the max of the absolute difference between current and next co-ordinates and sum it up
    return sum(max(abs(a[k]-a[k+1]), abs(b[k]-b[k+1])) for k in range(len(a) - 1))


if __name__ == "__main__":
    _, *a = map(int, input("a=").split())
    _, *b = map(int, input("b=").split())
    print(min_steps(a, b))
