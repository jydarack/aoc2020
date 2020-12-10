from typing import List, Tuple
from collections import Counter, defaultdict


def get_inputs(fn: str = "toy") -> List:
    with open(f"../inputs/day10/{fn}inputs.txt", "r") as f:
        inpt = f.readlines()
    return [int(x.strip()) for x in inpt]


def get_jolt_chain(inpt: List) -> List[Counter]:
    inpt.sort()
    dev_jolt = inpt[-1] + 3
    out = Counter([j - i for i, j in zip([0] + inpt, inpt + [dev_jolt])])
    return [(gap, c) for gap, c in out.items()]


def get_all_chains(inpt: List) -> int:
    output = max(inpt) + 3
    inpt.append(0)
    inpt.append(output)

    num_ways = [0] * (output + 1)
    num_ways[0] = 1
    if 1 in inpt:
        num_ways[1] = 1
    if (2 in inpt) & (1 in inpt):
        num_ways[2] = 2
    elif 2 in inpt:
        num_ways[2] = 1

    for n in range(3, output + 1):
        if n not in inpt:
            continue
        num_ways[n] = num_ways[n - 1] + num_ways[n - 2] + num_ways[n - 3]
    return num_ways[output]


if __name__ == "__main__":
    toy = get_inputs()
    assert len(toy) == 11
    assert all(type(x) == int for x in toy)

    assert get_jolt_chain(toy) == [(1, 7), (3, 5)]

    assert get_all_chains(toy) == 8

    puzzle = get_inputs("puzzle")
    (_, n1), (_, n3) = get_jolt_chain(puzzle)
    print("Part 1 : ", n1 * n3)
    assert n1 * n3 == 2244
    puzzle = get_inputs("puzzle")
    part2 = get_all_chains(puzzle)
    assert part2 == 3947645370368
    print("Part 2 : ", part2)

