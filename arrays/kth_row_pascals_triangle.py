#  NOTE : k is 0 based. k = 0, corresponds to the row [1].


def pascals_helper(A):
    if A == 0:
        return [1]
    elif A == 1:
        return [1, 1]
    else:
        previous_list = pascals_helper(A-1)
        current_list = [previous_list[i] + previous_list[i+1] for i in range(len(previous_list) - 1)]
        current_list.append(1)
        current_list.insert(0, 1)
    return current_list


print(pascals_helper(3))
