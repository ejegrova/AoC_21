import utils


def rotate_dial(single_rotation, actual_position):
    """Rotate a dial by single rotation, count all the times when dial gets through 0."""
    # print(actual_position, single_rotation)
    global counter
    if single_rotation[0] == "L":
        position = actual_position - single_rotation[1]
        if actual_position > 0 >= position:
            rounds_circled = -position // 100
            counter += abs(rounds_circled + 1)
        elif actual_position == 0:
            rounds_circled = -position // 100
            counter += abs(rounds_circled)
        else:
            rounds_circled = position // 100
            counter += abs(rounds_circled)
        return position % 100
    else:
        position = actual_position + single_rotation[1]
        rounds_circled = position // 100
        counter += abs(rounds_circled)
        return position % 100


def extract_rotation(single_rotation):
    """Change the type from string to tuple, for example: L68 -> (L, 68)"""
    return single_rotation[0], int(single_rotation[1:])


if __name__ == "__main__":
    data = utils.load_data("real_data/01.txt")

    rotations = []
    for line in data:
        rotations.append(extract_rotation(line))

    pos = 50
    counter = 0
    for line in rotations:
        pos = rotate_dial(line, pos)

    print(f"The number of times the dial pointed to 0: {counter}")
