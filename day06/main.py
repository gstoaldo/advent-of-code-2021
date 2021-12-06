def clock(state, max_age=8, respawn_age=6):
    new_fish = state[0]

    def decrement_one(state):
        next_state = state
        for i in range(max_age):
            next_state[i] = state[i + 1]

        return next_state

    def create_fish(state, new_fish):
        new_state = state
        new_state[respawn_age] += new_fish
        new_state[max_age] = new_fish
        return new_state

    return create_fish(decrement_one(state), new_fish)


def run_simulation(input, days):
    state = parse_to_state(input)
    for _ in range(days):
        state = clock(state)

    return fish_count(state), state


def fish_count(state):
    return sum(state)


###


def parse(filename):
    with open(filename) as file:
        input = map(int, file.read().split(","))

    return list(input)


def parse_to_state(input, max_age=8):
    state = [0 for _ in range(max_age + 1)]
    for i, _ in enumerate(state):
        state[i] = len([timer for timer in input if timer == i])

    return state


def solve(filename):
    input = parse(filename)
    part1, _ = run_simulation(input, 80)
    part2, _ = run_simulation(input, 256)

    return part1, part2


if __name__ == "__main__":
    part1, part2 = solve("input.txt")
    print(f"part1: {part1}")
    print(f"part1: {part2}")
