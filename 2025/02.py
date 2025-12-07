import utils
import sys


def split_range(ranges):
    """Split all the range into list of lists, removing the dash."""
    separated_range_values = []
    for range in ranges:
        separated_range_values.append(range.split(sep="-"))
    return separated_range_values


def invalid_ids_within_range(range_values):
    """Get range of values and get the invalid ones."""
    invalid_ids = []
    for value in range_values:
        value_length = len(value)
        for chunk_size in range(1, value_length):
            if value_length % chunk_size:
                continue

            separate_strings = [
                value[i : i + chunk_size] for i in range(0, value_length, chunk_size)
            ]
            if all(chunks == separate_strings[0] for chunks in separate_strings):
                invalid_ids.append(int(value))

    return set(invalid_ids)


def generate_ids_within_range(range_values):
    """Get range of values and generate all the values in between."""
    num1 = int(range_values[0])
    num2 = int(range_values[1])
    generated_values = list(range(num1, num2 + 1))
    generated_values = list(map(str, generated_values))
    return generated_values


if __name__ == "__main__":

    if sys.argv[-1] == "--test":
        data = utils.load_single_line_data("first_data/02.txt", ",")
    else:
        data = utils.load_single_line_data("real_data/02.txt", ",")

    split_ranges = split_range(data)

    generated_ranges = []
    for range_values in split_ranges:
        generated_ranges.append(generate_ids_within_range(range_values))

    invalid_ids = []
    for range_values in generated_ranges:
        invalid_ids.extend(invalid_ids_within_range(range_values))

    print(f"sum of invalid ids: {sum(invalid_ids)}")
