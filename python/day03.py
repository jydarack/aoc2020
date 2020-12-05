from typing import Tuple, List
from math import prod


def run(my_map: List[str], slope: Tuple = (3, 1), start: Tuple = (0, 0)) -> List:
    """
    The Tobbogan Slide function.
    Why did I do it with a recursion, I have no idea
    Also happy to have done the parameterisation of the slope in part 1.
    No rework needed in part 2
    """
    x, y = start
    right, down = slope
    height, wdth = len(my_map), len(my_map[0])

    new_x = (x + right) % wdth
    new_y = min(height - 1, (y + down))

    mark = [my_map[new_y][new_x]]

    if new_y >= height - 1:
        return mark
    else:
        mark += run(my_map, slope, start=(new_x, new_y))
        return mark


def get_map(fn: str = "toy") -> List[List[str]]:
    """
    Getting the map itself.
    Not sure if using a 2x2 list is actually useful as we can directly
    index the strings...
    """
    with open(f"../inputs/day03/{fn}inputs.txt", "r") as f:
        my_map = [list(x.strip()) for x in f.readlines()]
    return my_map


if __name__ == "__main__":
    my_map = get_map()
    assert my_map[0] == [".", ".", "#", "#", ".", ".", ".", ".", ".", ".", "."]

    toy = sum([1 for x in run(my_map) if x == "#"])
    assert toy == 7

    slopes_part2 = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2),
    ]

    vld = []
    for slp in slopes_part2:
        k = sum(1 for x in run(my_map, slope=slp) if x == "#")
        vld.append(k)

    assert vld == [2, 7, 3, 4, 2]

    ## Part 1
    my_map = get_map("puzzle")
    part1 = toy = sum([1 for x in run(my_map) if x == "#"])
    print("This many trees (Part 1): ", part1)

    # Part 2
    vld = {}
    for slp in slopes_part2:
        k = sum(1 for x in run(my_map, slope=slp) if x == "#")
        vld[slp] = k

    print("This many trees (Part 2): ", vld)
    print("Answer part 2: ", prod(vld.values()))
