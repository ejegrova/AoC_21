def depth_increase(file):
    """
    counts how many times the depth has increased between consecutive measurements

    :param file: data of the submarine depth
    :return: number of times the depth has increased
    """
    with open(file, "r", ) as f:
        increased = 0
        previous = int(f.readline().strip())
        for line in f:
            depth = int(line.strip())
            if (depth - previous) > 0:
                increased += 1
            previous = depth
        return increased


def depth_increase_in_three_measurements(file):
    """
    counts how many times the depth has increased when comparing sum of three
    measurements with the next three three measurements,
    eg. for measurements nr. 1, 2, 3, 4 we would do sum of 1, 2, 3 and compare it with sum of 2, 3, 4

    :param file: data of the submarine depth
    :return: number of times the depth has increased
    """
    with open(file, "r", ) as f:
        increased = 0
        trio = []
        for line in f:
            if len(trio) < 3:
                trio.append(int(line.strip()))
                if len(trio) == 3:
                    previous_sum_depth = sum(trio)
                continue

            del trio[0]
            trio.append(int(line.strip()))
            suma_depth = sum(trio)
            if (suma_depth - previous_sum_depth) > 0:
                increased += 1
            previous_sum_depth = suma_depth
        return increased


if __name__ == "__main__":
    print(f"part 01 increased: {depth_increase('depth_data.txt')}x")
    print(f"part 02 increased: {depth_increase_in_three_measurements('depth_data.txt')}x")
