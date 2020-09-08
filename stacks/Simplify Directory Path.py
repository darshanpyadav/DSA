'''
Given a string A representing an absolute path for a file (Unix-style).

Return the string A after simplifying the absolute path.

Note:

Absolute path always begin with ’/’ ( root directory ).

Path will not have whitespace characters.



Input Format

The only argument given is string A.
Output Format

Return a string denoting the simplified absolue path for a file (Unix-style).
For Example

Input 1:
    A = "/home/"
Output 1:
    "/home"

Input 2:
    A = "/a/./b/../../c/"
Output 2:
    "/c"
'''


def simplifyPath(A):
    # i = 0
    # op = "./"
    # stack = []
    # while i < len(A):
    #     if A[i] not in op:
    #         s = ""
    #         while i < len(A) and A[i] not in op:
    #             s, i = s+A[i], i+1
    #         stack.append(s)
    #     else:
    #         if i+1 < len(A) and A[i:i+2] == ".." and len(stack) != 0:
    #             stack.pop()
    #     i += 1
    # return "/" + "/".join(stack)
    dirs = A.split('/')
    result = []
    for c in dirs:
        if c == '' or c == '.':
            continue
        elif c == '..':
            if len(result) > 0:
                result.pop()
        else:
            result.append(c)
    return '/'+'/'.join(result)


A = "/a/./b/../../c/"
A = "/fic/././iak/../../hgy/blg/../vzt/../tod/.././.././bsc/./krk/../lnb/zhj/./"
A = "/home/"
A = "/../"
A = "/cbj/vfb/dyj/../../hjq/./unc/./cmv/./axj/../pzg/svs/oja/./rlc/vyr/cqq/../omk/viy/kyb/../ygr/mbx/nom/yvh/./../././lyg/qjv/./lwm/.././.././xga/krs/../xkl/wtj/nml/dal/hat/alw/jvo/./../xts/nul/yfe/upg/zhy/nzo/dtp/nqt/hqk/./../ref/gms/zhp/./bpp/jis/ccc/bmn/iip/nfv/../vbk/ugr/gpd/uez/./bqt/zqy/../vuf/ltg/mxm/../lvr/vef/../wpp/./rbc/xii/pkf/jsx/././xwo"

print(simplifyPath(A))
