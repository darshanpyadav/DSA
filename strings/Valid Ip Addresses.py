'''
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

A valid IP address must be in the form of A.B.C.D, where A,B,C and D are numbers from 0-255. The numbers cannot be 0 prefixed unless they are 0.

Example:

Given “25525511135”,

return [“255.255.11.135”, “255.255.111.35”]. (Make sure the returned strings are sorted in order)
'''


def restoreIpAddresses(string):
    iterator = 1110
    res = []
    # min lengths of each string is 1,1,1,1
    # Loop through each length and check if it's a valid IP
    # lengths of each sting can be max 3,3,3,3
    # will run 81 times
    while iterator != 3333:
        iterator += 1
        str_iterator = str(iterator)
        a, b, c, d = int(str_iterator[0]), int(str_iterator[1]), int(str_iterator[2]), int(str_iterator[3])
        if d == 4:
            if c != 3:
                c, d = c+1, 1
                d = 1
            elif b != 3:
                b, c, d = b+1, 1, 1
            else:
                a, b, c, d = a+1, 1, 1, 1
            iterator = int(str(a) + str(b) + str(c) + str(d))
        try:
            if a + b + c + d < len(string):
                continue
            string1, string2, string3, string4 = string[:a], string[a:a+b], string[a+b:a+b+c], string[a+b+c:]

            # if a valid number has trailing 0s they are invalid
            if (int(string1) > 0 and string1[0] == "0") or (int(string2) > 0 and string2[0] == "0") or \
                    (int(string3) > 0 and string3[0] == "0") or (int(string4) > 0 and string4[0] == "0"):
                continue

            # if a number is 0 and has trailing 0s, it's invalid
            if (int(string1) == 0 and len(string1) > 1) or (int(string2) == 0 and len(string2) > 1) \
                    or (int(string3) == 0 and len(string3) > 1) or (int(string4) == 0 and len(string4) > 1):
                continue

            if (0 <= int(string1) <= 255) and (0 <= int(string2) <= 255) and \
                    (0 <= int(string3) <= 255) and (0 <= int(string4) <= 255):
                res_str = string1 + "." + string2 + "." + string3 + "." + string4
                if res_str not in res:
                    res.append(res_str)
        except Exception:
            continue
    return res


# print(restoreIpAddresses("25525511135"))
print(restoreIpAddresses("010010"))
