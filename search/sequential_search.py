

# Best = 1
# Average = n/2
# Worst = n
def search(l, item):
    for i in l:
        if i == item:
            return True
    return False


# List is sorted
# Best = 1
# Average  = n/2
# Worst = n
# Better use when item is not present
def ordered_search(l, item):
    for i in l:
        if i == item:
            return True
        if i > item:
            return False
    return False
