import utils


def elf_calories(all_calories):
    """
    Get total number of calories that the elves are carrying
    :param all_calories:  list with calories for each food
    :return: list with calories that every elf carry
    """
    single_elf = 0
    elves = []
    for index, single_food in enumerate(all_calories):
        if single_food == "":
            elves.append(single_elf)
            single_elf = 0
            continue
        if single_food != "" and index == len(all_calories) - 1:
            single_elf += int(single_food)
            elves.append(single_elf)
        single_elf += int(single_food)
    return elves

def elf_with_most_calories(elves):
    """
    Get position of elf that carry the most calories
    :param elves: list with calories that every elf carry
    :return: elf that carry the most calories
    :rtype: tuple
    """
    calories = max(elves)
    elf = elves.index(max(elves))
    return elf, calories

def find_three_elves_with_most_calories(elves):
    """
    Get 3 elves that carry the most calories
    :param elves: list with calories that every elf carry
    :return: three elves positions and their calories
    :rtype: list of tuples
    """
    three_elves = []
    for i in range(3):
        elf = elf_with_most_calories(elves)
        elves.pop(elf[0])
        elf = (elf[0]+1, elf[1])
        three_elves.append(elf)
    return three_elves


if __name__ == "__main__":
    # file = "test_01.txt"
    file = "01.txt"
    all_calories = utils.load_data(file)
    elves = elf_calories(all_calories)
    elf, calories = elf_with_most_calories(elves)
    print(f"elf {elf} carry {calories} calories")

    three_elves = find_three_elves_with_most_calories(elves)
    combined_calories = sum(j for i, j in three_elves)
    print(f"sum of calories that 3 elves carry: {combined_calories}")
