from typing import List, Tuple
from copy import deepcopy
from math import sin, cos, radians, floor

compass = {0: "N", 1: "E", 2: "S", 3: "W"}
rev_compass = {y: x for x, y in compass.items()}


def get_inputs(fn: str = "toy") -> List:
    with open(f"../inputs/day12/{fn}inputs.txt") as f:
        inpt = f.readlines()

    return [(x[0], int(x[1:])) for x in inpt]


def follow_path(inpt: List, init: str, coords=(0, 0)) -> Tuple:
    for dir, amnt in inpt:
        if dir == "F":
            dir = deepcopy(init)

        if dir == "N":
            coords = (coords[0] + amnt, coords[1])
        elif dir == "E":
            coords = (coords[0], coords[1] + amnt)
        elif dir == "S":
            coords = (coords[0] - amnt, coords[1])
        elif dir == "W":
            coords = (coords[0], coords[1] - amnt)
        elif dir == "R":
            offset = (rev_compass[init] + amnt // 90) % 4
            init = compass[offset]
        elif dir == "L":
            offset = abs(rev_compass[init] + (360 - amnt) // 90) % 4
            init = compass[offset]

    return coords


def rotate(waypoint: Tuple, angledeg: int) -> Tuple:
    mat = [
        [cos(radians(angledeg)), -sin(radians(angledeg))],
        [sin(radians(angledeg)), cos(radians(angledeg))],
    ]
    mat = [[floor(y) for y in x] for x in mat]
    out = (
        waypoint[0] * mat[0][0] + waypoint[1] * mat[1][0],
        waypoint[0] * mat[0][1] + waypoint[1] * mat[1][1],
    )
    return out


def follow_waypoint(
    inpt: List, boat: Tuple = (0, 0), waypoint: Tuple = (1, 10)
) -> Tuple:
    for dir, amnt in inpt:
        if dir == "F":
            boat = (boat[0] + amnt * waypoint[0], boat[1] + amnt * waypoint[1])
        elif dir == "N":
            waypoint = (waypoint[0], waypoint[1] + amnt)
        elif dir == "E":
            waypoint = (waypoint[0] + amnt, waypoint[1])
        elif dir == "S":
            waypoint = (waypoint[0], waypoint[1] - amnt)
        elif dir == "W":
            waypoint = (waypoint[0] - amnt, waypoint[1])
        elif dir == "R":
            waypoint = rotate(waypoint, amnt)
        elif dir == "L":
            waypoint = rotate(waypoint, -1 * amnt)
        # print(boat,waypoint)
    return boat


def manhattan(coords: Tuple) -> int:
    return abs(coords[0]) + abs(coords[1])


if __name__ == "__main__":
    toy = get_inputs()
    assert len(toy) == 5
    assert manhattan(follow_path(toy, "E")) == 25

    puzzle = get_inputs("puzzle")
    part1 = follow_path(puzzle, "E")
    print("Part 1: ", manhattan(part1))

    assert rotate((10, 4), 90) == (4, -10)
    assert rotate((10, 4), -90) == (-4, 10)

    assert manhattan(follow_waypoint(toy, (0, 0), (10, 1))) == 286
    part2 = follow_waypoint(puzzle, (0, 0), (10, 1))
    print("Part 2: ", manhattan(part2))

