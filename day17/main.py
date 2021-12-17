def vx(v0, t):
    return max(0, v0 - t)


def vy(v0, t):
    return v0 - t


def s_eq(s0, v0, t, v_eq):
    if t == 0:
        return s0

    return v_eq(v0, t - 1) + s_eq(s0, v0, t - 1, v_eq)


def xt(x0, v0, t):
    return s_eq(x0, v0, t, vx)


def yt(x0, v0, t):
    return s_eq(x0, v0, t, vy)


def hits_target(vx0, vy0, target, x0=0, y0=0):
    t = 0
    tx, ty = target

    tx_min, tx_max = min(tx), max(tx)
    ty_min, ty_max = min(ty), max(ty)

    max_y = 0

    while True:
        x, y = xt(x0, vx0, t), yt(y0, vy0, t)

        max_y = max(max_y, y)

        if x > tx_max:
            return False, None
        if y < ty_min:
            return False, None

        if x >= tx_min and y <= ty_max:
            return True, max_y

        t += 1


def throw_with_style(target, max_vy0=100):
    tx, ty = target
    throws = []
    for vx0 in range(max(tx) + 1):
        for vy0 in range(min(ty) - 1, max_vy0):
            hits, max_y = hits_target(vx0, vy0, target)

            if hits:
                throws.append(max_y)

    return max(throws), len(throws)


###


def solve(target):
    part1, part2 = throw_with_style(target)
    return part1, part2


if __name__ == "__main__":
    INPUT = ((277, 318), (-92, -53))

    part1, part2 = solve(INPUT)
    print(f"part1: {part1}")
    print(f"part2: {part2}")
