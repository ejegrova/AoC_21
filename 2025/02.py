import utils


def split_range(ranges):
    """Split all the range into list of lists, removing the dash."""
    separated_range_values = []
    for range in ranges:
        separated_range_values.append(range.split(sep="-"))
    return separated_range_values


def invalid_ids_within_range(range_values):
    """Get range of values and get the invalid ones."""

    def split_string_in_half(string_number):
        """Get 2 strings split in half from the input."""
        chunk_size = len(string_number) // 2
        return [
            string_number[i: i + chunk_size]
            for i in range(0, len(string_number), chunk_size)
        ]

    invalid_ids = []
    for value in range_values:
        if len(value) % 2 == 0:
            two_strings = split_string_in_half(value)
            if two_strings[0] == two_strings[1]:
                invalid_ids.append(int(value))
    return invalid_ids


def generate_ids_within_range(range_values):
    """Get range of values and generate all the values in between."""
    num1 = int(range_values[0])
    num2 = int(range_values[1])
    generated_values = list(range(num1, num2 + 1))
    generated_values = list(map(str, generated_values))
    return generated_values


if __name__ == "__main__":
    data = utils.load_single_line_data("real_data/02.txt", ",")

    split_ranges = split_range(data)

    generated_ranges = []
    for range_values in split_ranges:
        generated_ranges.append(generate_ids_within_range(range_values))

    invalid_ids = []
    for range_values in generated_ranges:
        invalid_ids.extend(invalid_ids_within_range(range_values))

    print(f"sum of invalid ids: {sum(invalid_ids)}")
