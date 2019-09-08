def reverse(s):
    if not s:
        return s
    if len(s) == 1:
        return s[0]
    else:
        return s[-1] + reverse(s[:-1])


print(reverse("hello"))
