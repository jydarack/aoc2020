from __future__ import annotations

from typing import Tuple, List
from math import ceil
from functools import reduce


def get_inputs(fn: str = "toy") -> Tuple[int, List]:
    with open(f"../inputs/day13/{fn}inputs.txt") as f:
        inpt = f.readlines()

    early = int(inpt[0])
    buses = [int(x) if x != "x" else x for x in inpt[1].split(",")]

    return (early, buses)


def get_earliest_bus(schedule: Tuple) -> int:
    early, ids = schedule
    ids = [x for x in ids if x != "x"]
    k = {x: x * ceil(early / x) - early for x in ids}
    m = min(k, key=k.get)
    return m * k[m]


## Chinese remainder. Thank you J. Gruss
def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a * b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1


def get_schedules(schedule: Tuple):
    _, schedule = schedule
    delta = [(x, (x - i) % x) for i, x in enumerate(schedule) if x != "x"]
    n, a = zip(*delta)
    return chinese_remainder(n, a)


if __name__ == "__main__":
    t_early, t_bus = get_inputs()
    assert get_earliest_bus((t_early, t_bus)) == 295
    assert get_schedules((t_early, t_bus)) == 1068781

    puzzle = get_inputs("puzzle")
    part1 = get_earliest_bus(puzzle)
    print("Part 1 : ", part1)
    part2 = get_schedules(puzzle)
    print("Part 2 : ", part2)
