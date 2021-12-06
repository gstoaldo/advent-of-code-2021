def clock(state):
    def decrement_one(state):
        return [timer - 1 for timer in state]

    def create_fish(state):
        return [*state, *[8 for timer in state if timer == -1]]

    def normalize(state):
        return [6 if timer == -1 else timer for timer in state]

    return normalize(create_fish(decrement_one(state)))


def run_simulation(initial_state, days):
    state = initial_state
    for _ in range(days):
        state = clock(state)

    return fish_count(state), state


def fish_count(state):
    return len(state)


###


def parse(filename):
    with open(filename) as file:
        input = map(int, file.read().split(","))

    return list(input)


def solve(filename):
    input = parse(filename)
    part1, _ = run_simulation(input, 80)
    return part1


if __name__ == "__main__":
    part1 = solve("input.txt")
    print(f"part1: {part1}")
