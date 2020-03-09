def pascals(A):
    _, r = pascals_helper(A)
    return r


def pascals_helper(A):
    if A == 0:
        return [], []
    elif A == 1:
        return [1], [[1]]
    elif A == 2:
        return [1, 1], [[1], [1, 1]]
    else:
        previous_list, r = pascals_helper(A-1)
        current_list = [previous_list[i] + previous_list[i+1] for i in range(len(previous_list) - 1)]
        current_list.append(1)
        current_list.insert(0, 1)
        r.append(current_list)
    return current_list, r


print(pascals(7))
