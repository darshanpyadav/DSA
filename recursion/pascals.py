      # 1
    # 1    1
   # 1    2    1
  # 1    3    3    1
 # 1    4    6    4    1
# 1    5    10    10    5    1


def pascals_triangle(n):
    if n == 1:
        print("[1]")
        return []
    else:
        prev_pascal_list = pascals_triangle(n-1)
        pascal_list = [prev_pascal_list[i] + prev_pascal_list[i + 1] for i in range(len(prev_pascal_list) - 1)]
        pascal_list.insert(0, 1)
        pascal_list.append(1)
        print(pascal_list, sep=" ")
        return pascal_list
        

pascals_triangle(7)
