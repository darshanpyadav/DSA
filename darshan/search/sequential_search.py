# Average time complexity
# present = n/2
# absent = n
def search(l, item):
    for i in l:
        if i == item:
            return True
    return False


# List is sorted
# Average time complexity
# present = absent = n/2
def ordered_search(l, item):
    for i in l:
        if i == item:
            return True
        if i > item:
            return False
    return False
