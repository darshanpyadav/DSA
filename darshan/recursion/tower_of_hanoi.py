def tower_of_hanoi(height, from_pole, with_pole, to_pole):
    if height >= 1:
        tower_of_hanoi(height-1, from_pole, to_pole, with_pole)
        move_disk(from_pole, to_pole)
        tower_of_hanoi(height-1, with_pole, from_pole, to_pole)


def move_disk(fp, tp):
    print("moving disk from", fp, "to", tp)


tower_of_hanoi(3, "A", "B", "C")
