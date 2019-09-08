from collections import defaultdict

visited = defaultdict(lambda: False)
jug1, jug2, aim = int(input("Jug 1")), int(input("Jug2")), int(input("aim"))

# Empty the first jug completely
# Empty the second jug completely
# Fill the first jug
# Fill the second jug
# Fill the water from the second jug into the first jug until the first jug is full or the second jug has no water left
# Fill the water from the first jug into the second jug until the second jug is full or the first jug has no water left


def water_jug(amt1, amt2):
    if (amt1 == aim and amt2 == 0) or (amt2 == aim and amt1 == 0):
        return True
    else:
        if not visited[(amt1, amt2)]:
            visited[(amt1, amt2)] = True
            print(amt1, amt2, sep=" ")
            return water_jug(0, amt2) or water_jug(amt1, 0) or water_jug(jug1, amt2) or water_jug(amt1, jug2) or \
                   water_jug(amt1 + min(amt2, jug1 - amt1), amt2 - min(amt2, jug1 - amt1)) or \
                   water_jug(amt1 - min(amt1, jug2 - amt2), amt2 + min(amt1, jug2 - amt2))
        else:
            return False


water_jug(0, 0)
