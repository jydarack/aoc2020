from typing import List, Tuple, Dict
from collections import Counter
from pprint import PrettyPrinter

pp = PrettyPrinter(indent=4)

SEATING = {".": "Floor", "L": "Empty seat", "#": "Occupied seat"}


def get_inputs(fn: str = "toy") -> Dict:
    with open(f"../inputs/day11/{fn}inputs.txt", "r") as f:
        inpt = f.readlines()

    return {
        (x, y): "L"
        for x, l in enumerate(inpt)
        for y, _ in enumerate(l)
        if inpt[x][y] == "L"
    }


def get_adjacent(seating: Dict, coords: Tuple) -> Counter:
    # adjacent = 8 positions directly around the seat considered
    x, y = coords
    delta = [-1, 0, 1]
    k = [(x + dx, y + dy) for dx in delta for dy in delta]

    return Counter([seating.get(x) for x in k if seating.get(x, False)])


def do_seating_round(seats: Dict):
    out = {}
    for coords in seats:
        if (seats[coords] == "L") & (get_adjacent(seats, coords).get("#", 0) == 0):
            out[coords] = "#"
        elif (seats[coords] == "#") & (get_adjacent(seats, coords).get("#", 0) >= 4):
            out[coords] = "L"
        else:
            out[coords] = seats[coords]

    return out


def get_occupancy(seats: Dict) -> int:
    return sum(1 for x in seats.values() if x == "#")


if __name__ == "__main__":
    toy = get_inputs()
    # print(get_adjacent(toy, (0, 0)))
    i = 1
    while True:
        print("Round ", i)
        out = do_seating_round(toy)
        if all(toy[coords] == out[coords] for coords in toy.keys()):
            break
        else:
            print(get_occupancy(out))
            input()
            toy = out
            i += 1
    pp.pprint(out)

    ## Toy solution osciliating between 2 states and I can't find the issue...

