### part1

LEN_UNIQUE = set([2, 3, 4, 7])


def count_unique_segments(output_values):
    return len([digit for digit in output_values if len(digit) in LEN_UNIQUE])


def count_output_unique_segments(input):
    return sum(count_unique_segments(output) for _, output in input)


### part2

SEGMENTS = ["a", "b", "c", "d", "e", "f", "g"]

DIGITS = [
    ("abcefg", 0),
    ("cf", 1),
    ("acdeg", 2),
    ("acdfg", 3),
    ("bcdf", 4),
    ("abdfg", 5),
    ("abdefg", 6),
    ("acf", 7),
    ("abcdefg", 8),
    ("abcdfg", 9),
]


def segment_freq(signals):
    count = {segment: 0 for segment in SEGMENTS}
    for signal in signals:
        for segment in signal:
            count[segment] += 1

    return count


def segment_by_count(signals, count, filter=[]):
    return [
        key
        for key, value in segment_freq(signals).items()
        if value == count and key not in filter
    ]


def signal_by_length(signals, length):
    return [signal for signal in signals if len(signal) == length][0]


def map_f(signals):
    return segment_by_count(signals, 9)[0]


def map_e(signals):
    return segment_by_count(signals, 4)[0]


def map_b(signals):
    return segment_by_count(signals, 6)[0]


def map_c(segments_map, signals):
    one_signal = signal_by_length(signals, 2)
    for segment in one_signal:
        if segment != segments_map["f"]:
            return segment


def map_a(segments_map, signals):
    filter = [segments_map["c"]]
    return segment_by_count(signals, 8, filter)[0]


def map_d(segments_map, signals):
    four_signal = signal_by_length(signals, 4)

    for segment in four_signal:
        if segment not in segments_map.values():
            return segment


def map_g(segments_map):
    for segment in SEGMENTS:
        if segment not in segments_map.values():
            return segment


def map_segments(signals):
    segments_map = {segment: None for segment in SEGMENTS}
    segments_map["f"] = map_f(signals)
    segments_map["e"] = map_e(signals)
    segments_map["b"] = map_b(signals)
    segments_map["c"] = map_c(segments_map, signals)
    segments_map["a"] = map_a(segments_map, signals)
    segments_map["d"] = map_d(segments_map, signals)
    segments_map["g"] = map_g(segments_map)

    return segments_map


def get_signals_translation(signals):
    segments_map = map_segments(signals)
    digits = translate_digits(segments_map)
    translation = {}

    for signal in signals:
        for key, value in digits.items():
            if len(key) == len(signal):
                if all([segment in signal for segment in key]):
                    translation[signal] = value

    return translation


def translate_digits(segments_map):
    translated = {}
    for digit, number in DIGITS:
        translated_digit = ""
        for segment in digit:
            translated_digit += segments_map[segment]

        translated[translated_digit] = number

    return translated


def sum_outputs(input):
    output_sum = 0

    for signals, output in input:
        signals_translation = get_signals_translation(signals)

        number_digits = []

        for signal in output:
            number_digits.append(str(get_digit(signals_translation, signal)))

        number = int("".join(number_digits))

        output_sum += number

    return output_sum


def get_digit(signals_translation, signal):
    for key, value in signals_translation.items():
        if len(key) == len(signal):
            if all([segment in signal for segment in key]):
                return value


###


def parse(filename):
    def parse_line(line):
        return tuple(map(lambda x: x.strip().split(" "), line.split("|")))

    with open(filename) as file:
        input = map(parse_line, file.readlines())

    return list(input)


def solve(filename):
    input = parse(filename)
    part1 = count_output_unique_segments(input)
    part2 = sum_outputs(input)

    return part1, part2


if __name__ == "__main__":
    part1, part2 = solve("input.txt")
    print(f"part1: {part1}")
    print(f"part2: {part2}")
