DARK = "."
LIGHT = "#"

BINARY = {DARK: "0", LIGHT: "1"}


def add_margin(initial_img, margin=3, filler=DARK):
    height = len(initial_img) + 2 * margin
    width = len(initial_img[0]) + 2 * margin

    img = []
    for i in range(height):
        row = []
        if i < margin or i > height - margin - 1:
            row = [filler] * width
        else:
            row = [
                *[filler] * margin,
                *initial_img[i - margin],
                *[filler] * margin,
            ]
        img.append(row)

    return img


def square(img, pi, pj, size=3, filler=DARK):
    delta = (size - 1) // 2

    pixels = []
    for i in range(size):
        si = pi - delta + i
        for j in range(size):
            sj = pj - delta + j
            if 0 <= si < len(img) and 0 <= sj < len(img[0]):
                pixels.append(img[si][sj])
            else:
                pixels.append(filler)

    return "".join(pixels)


def pixels_to_decimal(pixels):
    return int("".join(BINARY[pixel] for pixel in pixels), 2)


def enhance(img, alg):
    enhanced_img = []
    for i, _row in enumerate(img):
        row = []
        for j, _ in enumerate(_row):
            index = pixels_to_decimal(square(img, i, j))
            row.append(alg[index])
        enhanced_img.append(row)

    return enhanced_img


def process(img, alg, n):
    img = add_margin(img, 6 * n)
    for i in range(n):
        img = enhance(img, alg)
        img = trim(img)

        # for row in img:
        #     print("".join(row))

    return img


def count_light_pixels(img):
    return sum(sum(1 for pixel in row if pixel == LIGHT) for row in img)


def solve_part1(alg, img, n=2):
    img = process(img, alg, n)

    return count_light_pixels(img)


def trim(img):
    return [row[1:] for row in img[1:]]


###


def parse(filename):
    with open(filename) as file:
        _algo, _img = file.read().split("\n\n")
        alg = _algo.strip()
        img = [[pixel for pixel in row] for row in _img.splitlines()]

    return alg, img


def solve(filename):
    alg, img = parse(filename)

    part1 = solve_part1(alg, img, n=2)
    part2 = solve_part1(alg, img, n=50)

    return part1, part2


if __name__ == "__main__":
    part1, part2 = solve("input.txt")
    print(f"part1: {part1}")
    print(f"part2: {part2}")
