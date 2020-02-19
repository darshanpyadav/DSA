
# *****************************************************************************
# Author            : darshanp (darshanp@juniper.net)
# Date              : 14/09/19
# Last modified by  : darshanp
# Version           : 1.0
# Description       : Let-s-do-it
# *****************************************************************************
# Given a number represented as an array of digits,
#
# add 1 to the number ( increment the number represented by the digits ).
#
# The digits are stored such that the most significant digit is at the head of the list.
#
# Example:
#
# If the vector has [1, 2, 3]
#
# the returned vector should be [1, 2, 4]
#
# as 123 + 1 = 124.


def add_one_to_number(a):
    int_a = int("".join(map(str, a)))
    if int_a + 1 < 0:
        l = list(map(int, list(str(int_a + 1))[1:]))
        l[0] = l[0]*-1
        return l
    return list(map(int, list(str(int_a + 1))))


if __name__ == "__main__":
    _, *a = map(int, input("a=").split())
    print(add_one_to_number(a))

# O(1)
