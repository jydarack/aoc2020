from typing import List


def get_inputs(fn: str = "toy") -> List[int]:
    with open(f"../inputs/day09/{fn}inputs.txt", "r") as f:
        inpt = f.readlines()
    return [int(x.strip()) for x in inpt]


def XMAS_fail_check(data: List[int], preamble: int = 25) -> int:
    for i, val in enumerate(data[preamble:]):
        # slice stops at 1 before last and that's OK
        # because last will be the last Item to check
        my_pre = set(data[i : i + preamble])
        k = {val for x in my_pre for y in my_pre if x != y and val == (x + y)}
        if not k:
            return val


def crack_XMAS(data: List, inpt: int) -> int:
    i = data.index(inpt)
    for s in range(i):
        if data[s] > inpt:
            continue
        for e in range(s + 1, i + 1):
            if sum(data[s:e]) > inpt:
                break
            if sum(data[s:e]) == inpt:
                cont = data[s:e]
                return max(cont) + min(cont)


if __name__ == "__main__":
    toy = get_inputs()
    assert len(toy) == 20
    assert all([type(x) == int for x in toy])

    assert XMAS_fail_check(toy, 5) == 127

    assert crack_XMAS(toy, 127) == 62

    puzzle = get_inputs("puzzle")
    part1 = XMAS_fail_check(puzzle, 25)
    print("Part 1: ", part1)
    assert part1 == 248131121

    part2 = crack_XMAS(puzzle, part1)
    print("Part 2: ", part2)
    assert part2 == 31580383
