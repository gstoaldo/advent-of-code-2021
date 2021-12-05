from operator import attrgetter


class Board:
    def __init__(self, data):
        self.board = [[n for n in row] for row in data]
        self.marks = [[False for _ in row] for row in data]
        self.is_bingo = False
        self.bingo_number = None
        self.round = 0

    def mark(self, call_number, round=0):
        if self.is_bingo:
            return

        for i, row in enumerate(self.board):
            for j, value in enumerate(row):
                if value == call_number:
                    self.marks[i][j] = True

        if self.bingo():
            self.is_bingo = True
            self.bingo_number = call_number
            self.round = round

    def bingo(self):
        for i, _ in enumerate(self.board):
            if all(self.marks[i]):
                return True

        for j, _ in enumerate(self.board[0]):
            if all(row[j] for row in self.marks):
                return True

        return False

    def unmarked_sum(self):
        return sum(
            sum(n for j, n in enumerate(row) if not self.marks[i][j])
            for i, row in enumerate(self.board)
        )


def calc_first_bingo(number_calls, boards_data):
    boards = [Board(data) for data in boards_data]

    for number_call in number_calls:
        for board in boards:
            board.mark(number_call)
            if board.bingo():
                return number_call, board.unmarked_sum()

    return False


def calc_last_bingo(number_calls, boards_data):
    boards = [Board(data) for data in boards_data]

    for round, number_call in enumerate(number_calls):
        for board in boards:
            board.mark(number_call, round)

        not_bingo_boards = [board for board in boards if not board.bingo()]

        if len(not_bingo_boards) == 0:
            break

    last_board = max(boards, key=attrgetter("round"))

    return last_board.bingo_number, last_board.unmarked_sum()


def calc_score(number_calls, boards_data, func):
    last_call, unmarked_sum = func(number_calls, boards_data)

    return last_call * unmarked_sum


def read_file(filename):
    with open(filename) as file:
        lines = file.readlines()

        calls = [int(n) for n in lines[0].split(",")]

        boards = []
        board = []

        for line in lines[2:]:
            if len(line) == 1:
                boards.append(board)
                board = []
            else:
                board.append([int(n) for n in line.split()])

        boards.append(board)

    return calls, list(boards)


def solve(filename):
    calls, boards = read_file(filename)

    part1_answer = calc_score(calls, boards, calc_first_bingo)
    part2_answer = calc_score(calls, boards, calc_last_bingo)

    return part1_answer, part2_answer


if __name__ == "__main__":
    part1_answer, part2_answer = solve("input.txt")
    print(f"part1: {part1_answer}")
    print(f"part2: {part2_answer}")
