from typing import List, Tuple

ROWS = {"F": 0, "B": 1}
SEATS = {"L": 0, "R": 1}


def get_boarding(fn: str = "toy") -> List:
    with open(f"../inputs/day05/{fn}inputs.txt", "r") as f:
        inpt = [x.strip() for x in f.readlines()]
    return inpt


def get_row_col(bp: str, nrows: int = 128, ncols: int = 8) -> Tuple:
    rcode, ccode = bp[:7], bp[-3:]
    rows = list(range(nrows))
    seats = list(range(ncols))
    for pos in rcode:
        l = len(rows) // 2
        k = [rows[:l], rows[l:]]
        rows = k[ROWS[pos]]
    for pos in ccode:
        l = len(seats) // 2
        k = [seats[:l], seats[l:]]
        seats = k[SEATS[pos]]
    return rows.pop(), seats.pop()


def seat_number(pos: Tuple) -> int:
    row, col = pos
    return row * 8 + col


if __name__ == "__main__":
    boarding_passes = get_boarding()
    toy = [get_row_col(x) for x in boarding_passes]
    toy_nums = [seat_number(x) for x in toy]
    assert toy == [(70, 7), (14, 7), (102, 4)]
    assert toy_nums == [567, 119, 820]

    puzzle = get_boarding("puzzle")
    all_bp = [seat_number(get_row_col(x)) for x in puzzle]
    print(
        "Max number on boarding pass: ", max(all_bp),
    )  ## 880

    ## Not using the hint in the directions
    ## Identifying all empty seats in the plane using set intersections
    k = set(range(min(all_bp), max(all_bp) + 1))
    print("Here is an empty seat: ", k - set(all_bp))

