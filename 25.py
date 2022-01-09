import copy


def load_data(file):
    """
    loads data from file to variable

    :param file: input file
    :return: positions of sea cucumbers and their direction
    :rtype: list of lists
    """
    with open(file, "r", ) as f:
        data = []
        for line in f:
            new_line = []
            for elem in line.strip():
                new_line.append(elem)
            data.append(new_line)
    return data


def move_sea_cucumbers(map):
    """
    Move sea cucumbers until they stop moving

    :param map: list of lists with positions of sea cucumbers and their direction
    :return: number of steps until sea cucumbers stop moving
    :rtype: int
    """
    step = 1
    sth_moved = True
    while sth_moved:
        sth_moved = False
        # move east
        new_map = copy.deepcopy(map)
        for j, line in enumerate(map):
            for i, elem in enumerate(line):
                if elem == '>':
                    try:
                        if line[i+1] == '.':
                            new_map[j][i] = '.'
                            new_map[j][i+1] = '>'
                            sth_moved = True
                    except IndexError:
                        if line[0] == '.':
                            new_map[j][i] = '.'
                            new_map[j][0] = '>'
                            sth_moved = True

        map = copy.deepcopy(new_map)
        # move south
        for j, line in enumerate(map):
            for i, elem in enumerate(line):
                if elem == 'v':
                    try:
                        if map[j+1][i] == '.':
                            new_map[j][i] = '.'
                            new_map[j+1][i] = 'v'
                            sth_moved = True
                    except IndexError:
                        if map[0][i] == '.':
                            new_map[j][i] = '.'
                            new_map[0][i] = 'v'
                            sth_moved = True

        map = copy.deepcopy(new_map)
        if sth_moved:
            step+=1

    return step


if __name__ == "__main__":
    map = load_data("25.txt")
    number_of_steps = move_sea_cucumbers(map)
    print(number_of_steps)

