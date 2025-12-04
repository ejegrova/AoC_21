def diagnose_power_consumption():
    """
    gamma rate in binary is the number we get after finding most common bit in every column of data
    epsilon rate in binary is the number we get after finding least common bit in every column of data

    :return: gamma rate, epsilon rate
    :rtype: int, int
    """
    gamma_rate_binary_list = []
    epsilon_rate_binary_list = []
    len_number = len(data[0])
    for i in range(len_number):
        mcb = most_common_bit(data, i)
        if mcb == "1":
            gamma_rate_binary_list.append(1)
            epsilon_rate_binary_list.append(0)
        else:
            gamma_rate_binary_list.append(0)
            epsilon_rate_binary_list.append(1)
    return convert_binary_list_to_decimal(gamma_rate_binary_list), \
        convert_binary_list_to_decimal(epsilon_rate_binary_list)


def most_common_bit(input_data, column):
    """
    get most common bit in column of data

    :param list input_data: binary inputs
    :param int column: order of the column in data
    :return: most common bit
    :rtype: str
    """
    one_count = number_count_in_column(input_data, column, "1")
    zero_count = number_count_in_column(input_data, column, "0")
    if one_count >= zero_count:
        return "1"
    else:
        return "0"


def number_count_in_column(input_data, column, number):
    """
    counts the total occurrence of number in the column

    :param input_data: binary inputs
    :param column: column of the data
    :param number: "1" or "0"
    :return: total count of number in the column
    """
    count = 0
    for line in input_data:
        num = line[column]
        if num == number:
            count += 1
    return count


def convert_binary_list_to_decimal(list_strings):
    """
    converts list of 1s and 0s to decimal number

    :param list_strings: list of characters 1s and 0s
    :return: decimal number
    """
    number_in_str = "".join([str(elem) for elem in list_strings])
    return int(number_in_str, 2)


def load_data(file):
    """
    loads data from file to variable

    :param file: input file
    :return: list of binary inputs
    """
    with open(file, "r", ) as f:
        data = []
        for line in f:
            data.append(line.strip())
    return data


def power_consumption(gamma, epsilon):
    """
    power consumption is gamma rate multiplied by epsilon rate
    """
    return gamma*epsilon


def co2_scrubber_rating():
    """
    To find CO2 scrubber rating, determine the least common value (0 or 1) in the current bit position from the data,
    and keep only numbers with that bit in that position.
    If 0 and 1 are equally common, keep values with a 0 in the position being considered.

    :return: co2 scrubber rating
    :rtype: int
    """
    co2_scrubber_rating_data = list(data)
    len_number = len(data[0])
    for i in range(len_number):
        mcb = most_common_bit(co2_scrubber_rating_data, i)
        if mcb == "0":
            co2_scrubber_rating_data = get_data_with_bit_in_column(co2_scrubber_rating_data, i, "1")
        elif mcb == "1":
            co2_scrubber_rating_data = get_data_with_bit_in_column(co2_scrubber_rating_data, i, "0")
        if len(co2_scrubber_rating_data) <= 1:
            break

    return convert_binary_list_to_decimal(co2_scrubber_rating_data)


def oxygen_generator_rating():
    """
    To find oxygen generator rating, determine the most common value (0 or 1) in the current bit position from the data,
    and keep only numbers with that bit in that position.
    If 0 and 1 are equally common, keep values with a 1 in the position being considered.

    :return: oxygen generator rating
    :rtype: int
    """
    oxygen_generator_rating_data = list(data)
    len_number = len(data[0])
    for i in range(len_number):
        mcb = most_common_bit(oxygen_generator_rating_data, i)
        oxygen_generator_rating_data = get_data_with_bit_in_column(oxygen_generator_rating_data, i, mcb)
        if len(oxygen_generator_rating_data) <= 1:
            break

    return convert_binary_list_to_decimal(oxygen_generator_rating_data)


def get_data_with_bit_in_column(input_data, column, bit):
    """
    preserve lines from the data that have bit value on column's position in the line

    :param list input_data: binary inputs
    :param column: column of the data
    :param bit: "1" or "0"
    :return: data which satisfies condition, bit is on column's position
    :rtype: list
    """
    new_data = []
    for line in input_data:
        if line[column] == bit:
            new_data.append(line)

    return new_data


def life_support_rating(oxygen, co2):
    """
    life support rating is oxygen generator rating multiplied by CO2 scrubber rating
    """
    return oxygen * co2


if __name__ == "__main__":
    data = load_data("diagnostic_data.txt")
    gamma, epsilon = diagnose_power_consumption()
    print(f"gamma rate: {gamma}")
    print(f"epsilon rate: {epsilon}")
    power = power_consumption(gamma, epsilon)
    print(f"power consumption: {power}")

    oxygen = oxygen_generator_rating()
    print(f"oxygen generator rating: {oxygen}")
    co2 = co2_scrubber_rating()
    print(f"co2 scrubber rating: {co2}")
    print(f"life support rating: {life_support_rating(oxygen, co2)}")
