import itertools as it
import numpy as np


def load_data(file):
    """
    loads data from file
    outputs sequence, that are drawed numbers for bingo
        and data that contains several bingo boards

    :param file: input file
    :return: sequence for bingo, bingo boards
    :rtype: list, list of lists
    """
    with open(file, "r", ) as f:
        data = []
        count = 0
        number_sequence = []
        for key, group in it.groupby(f, lambda line: line.startswith('\n')):
            bingo_board = [[[0 for _ in range(2)] for _ in range(5)] for _ in range(5)]
            if not key:
                single_board = list(group)
                if count == 0:
                    number_sequence = single_board[0].strip("\n").split(",")
                    number_sequence = list(map(int, number_sequence))
                    count += 1
                else:
                    single_board = [list(map(int, line.strip("\n").split())) for line in single_board]
                    for i, line in enumerate(single_board):
                        for j, elem in enumerate(line):
                            bingo_board[i][j] = [elem, 0]
                    data.append(np.array(bingo_board))

    return number_sequence, data


def draw_number(number):
    """
    Mark number in all boards

    :param int number: number to be marked in boards
    """
    for board in data:
        number_position = np.where(board[:, :, 0] == number)
        if number_position:
            change_number_to_drawed = (number_position[0], number_position[1], np.array([1]))
            board[change_number_to_drawed] = 1


def check_winner():
    """
    Checks if some of the board just won

    :return: bool value specifiyng if winner was found, winning board or empty list
    :rtype: bool, list
    """
    for board in data:
        for i in range(board.shape[0]):
            winner = np.all(board[i, :, 1] == 1)
            if winner:
                return winner, board
            winner = np.all(board[:, i, 1] == 1)
            if winner:
                return winner, board
    return False, []


def score(board, number):
    """
    Calculates score of the winning board.

    :param numpy.ndarray board: 5x5x2 grid, [][][1] sets the marked/unmarked number
    :param int number: number that finalized row or column in board (all marked)
    :return: total score for the board
    :rtype: int
    """
    undrawed_numbers = np.where(board[:, :, 1] == 0)
    if undrawed_numbers:
        sum = 0
        for i in range(len(undrawed_numbers[0])):
            undrawed_position = (undrawed_numbers[0][i], undrawed_numbers[1][i], 0)
            sum += board[undrawed_position]

    return sum * number


if __name__ == "__main__":
    sequence, data = load_data("bingo.txt")

    # part 01
    for num in sequence:
        draw_number(num)
        winner, board = check_winner()
        if winner:
            final_score = score(board, num)
            print(f"final score: {final_score}")
            break

    # part 02
    sequence, data = load_data("bingo.txt")
    for num in sequence:
        draw_number(num)
        winner, board = check_winner()
        final_scores = []
        while winner:
            remaining_boards = data.copy()
            # remove winning board from the data
            for i, _ in enumerate(remaining_boards):
                if np.array_equal(remaining_boards[i], board):
                    data.pop(i)
                    final_scores.append(score(board, num))
                    break
            winner, board = check_winner()

        if len(data) == 0:
            print(f"final score: {max(final_scores)}")
            break
