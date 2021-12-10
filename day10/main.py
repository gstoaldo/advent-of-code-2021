PAIRS = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}

SCORE = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}


def find_first_illegal_char(line):
    close_stack = []

    for char in line:
        if char in PAIRS:
            close_stack.append(PAIRS[char])
        elif char == close_stack[-1]:
            close_stack.pop()
        else:
            return char

    return None


def syntax_error_score(lines):
    illegal_chars = []
    for line in lines:
        if len(line) % 2 != 0:
            next

        illegal_char = find_first_illegal_char(line)
        if illegal_char != None:
            illegal_chars.append(illegal_char)

    return sum(SCORE[char] for char in illegal_chars)


def parse(filename):
    def parse_line(line):
        return line.strip()

    with open(filename) as file:
        input = map(parse_line, file.readlines())

    return list(input)


def solve(filename):
    input = parse(filename)
    part1 = syntax_error_score(input)

    return part1, None


if __name__ == "__main__":
    part1, part2 = solve("input.txt")
    print(f"part1: {part1}")
    print(f"part2: {part2}")
