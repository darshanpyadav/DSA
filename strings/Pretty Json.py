'''
Given a string A representating json object. Return an array of string denoting json object with proper indentaion.

Rules for proper indentaion:

Every inner brace should increase one indentation to the following lines.
Every close brace should decrease one indentation to the same line and the following lines.
The indents can be increased with an additional ‘\t’
Note:

[] and {} are only acceptable braces in this case.

Assume for this problem that space characters can be done away with.



Input Format

The only argument given is the integer array A.
Output Format

Return a list of strings, where each entry corresponds to a single line. The strings should not have "\n" character in them.
For Example

Input 1:
    A = "{A:"B",C:{D:"E",F:{G:"H",I:"J"}}}"
Output 1:
    {
        A:"B",
        C:
        {
            D:"E",
            F:
            {
                G:"H",
                I:"J"
            }
        }
    }

Input 2:
    A = ["foo", {"bar":["baz",null,1.0,2]}]
Output 2:
   [
        "foo",
        {
            "bar":
            [
                "baz",
                null,
                1.0,
                2
            ]
        }
    ]
'''


def prettyJSON(string):
    string = '{A:"B",C:{D:"E",F:{G:"H",I:"J"}}}'
    new_line = ["{", ",", "}", "[", "]"]
    open_indentation = ["{", "["]
    close_indentation = ["}", "]"]
    tab_count, prev_i, i = 0, -1, 0
    while i < len(string):
        if string[i] in new_line:
            print(string[i])
            if string[i] in open_indentation:
                tab_count += 1
                print("\t" * tab_count, end="")
            elif string[i] in close_indentation:
                tab_count -= 1
                print("\t" * tab_count)
            prev_i = i
            i += 1
        else:
            st = ""
            while (i < len(string)) and (string[i] not in new_line):
                st += string[i]
                prev_i = i
                i += 1
            print("\t" * tab_count + st, end="")


prettyJSON("asas")
