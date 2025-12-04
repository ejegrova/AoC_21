def load_data(file):
    """
    loads data from file to variable
    :param file: input file
    :return: list of binary inputs
    :rtype: list
    """
    with open(f"2025/{file}", "r", ) as f:
        data = []
        for line in f:
            data.append(line.strip())
    return data

