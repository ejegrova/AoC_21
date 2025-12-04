def easy_movement(movements, move, move_value):
    """
    changes the value for specific move in movements by adding move_value to the previous value

    :param dict movements: dictionary containing pairs move:value
    :param str move: specific key from the movements dict
    :param str move_value: value that is added to the move value in movements
    :return: movements with changed value for one move
    :rtype: dict
    """
    previous_value = int(movements[move])
    movements[move] = previous_value + int(move_value)

    return movements


def aim_based_movement(movements, move, move_value):
    """
    changes the value for specific attribute of the submarine

    moves (down, up, forward) does the following:
    down X increases your aim by X units.
    up X decreases your aim by X units.
    forward X does two things:
        It increases your horizontal position by X units.
        It increases your depth by your aim multiplied by X.

    :param dict movements: dictionary containing pairs attribute:value
    :param str move: specific move to be done
    :param str move_value: value of the move
    :return: movements with changed value for one attribute
    :rtype dict
    """
    if "forward" in move:
        value = movements["horizontal_position"]
        movements["horizontal_position"] = value + int(move_value)
        value = movements["depth"]
        movements["depth"] = value + movements["aim"] * int(move_value)
    elif "up" in move:
        value = movements["aim"]
        movements["aim"] = value - int(move_value)
    elif "down" in move:
        value = movements["aim"]
        movements["aim"] = value + int(move_value)

    return movements


def planned_course(horizontal_position, final_depth):
    """
    planned course is horizontal position multiplied by final depth
    """
    return horizontal_position * final_depth


if __name__ == "__main__":
    with open("movement_data.txt", "r", ) as f:
        easy_movements = {
            "forward": 0,
            "up": 0,
            "down": 0,
        }
        aim_movements = {
            "horizontal_position": 0,
            "depth": 0,
            "aim": 0,
        }

        for line in f:
            row = line.strip().split(' ')
            easy_movements = easy_movement(easy_movements, row[0], row[1])
            aim_movements = aim_based_movement(aim_movements, row[0], row[1])

        # part 01
        print(f"horizontal position: {easy_movements['forward']}")
        print(f"final depth: {easy_movements['down'] - easy_movements['up']}")
        final_depth_easy = easy_movements['down'] - easy_movements['up']
        print(f"planned course: {planned_course(easy_movements['forward'], final_depth_easy)}")

        # part 02
        print(f"horizontal position: {aim_movements['horizontal_position']}")
        print(f"final depth: {aim_movements['depth']}")
        print(f"planned course: {planned_course(aim_movements['horizontal_position'], aim_movements['depth'])}")
