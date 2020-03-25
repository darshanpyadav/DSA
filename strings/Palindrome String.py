'''
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Example:

"A man, a plan, a canal: Panama" is a palindrome.

"race a car" is not a palindrome.

Return 0 / 1 ( 0 for false, 1 for true ) for this problem
'''


def isPalindrome(string):
    start, end = 0, len(string)-1
    while start <= end:
        if not string[start].isalnum():
            start += 1
            continue
        if not string[end].isalnum():
            end -= 1
            continue
        if string[start].lower() != string[end].lower():
            return 0
        start, end = start+1, end-1
    return 1


string = "A man, a plan, a canal: Panama"
print(isPalindrome(string))