def remove_chars(f):
    def strip(s):
        s = "".join(i.lower() for i in s if i.isalpha())
        return f(s)
    return strip

@remove_chars
def palindrome(s):
    if len(s) < 2:
        return True
    if s[0] != s[-1]:
        return False
    return palindrome(s[1:-1])


print(palindrome("Reviled did I live, said I, as evil I did deliver"))