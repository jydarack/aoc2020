from typing import List, Tuple
from collections import Counter


def get_inputs(fn: str = "toy") -> List[str]:
    with open(f"../inputs/day06/{fn}inputs.txt", "r") as f:
        inpt = f.read().split("\n\n")
    return inpt


def check(ans: str) -> Tuple:
    ans = ans.replace("\n", "")
    return Counter(ans), len(set(ans))


def check2(ans: str) -> List:

    c, l = Counter(ans.replace("\n", "")), len(ans.split("\n"))
    k = [x for x, v in c.items() if v == l]

    return (k, len(k))


if __name__ == "__main__":
    toy = get_inputs()
    assert len(toy) == 5
    k = [check(x) for x in toy]
    assert [x[1] for x in k] == [3, 3, 3, 1, 1]

    k = [check2(x) for x in toy]
    assert [x[1] for x in k] == [3, 0, 1, 1, 1]

    puzzle = get_inputs("puzzle")
    print("Part 1: ", sum(check(x)[1] for x in puzzle))  # 6416
    print("Part 2: ", sum(check2(x)[1] for x in puzzle))  # 3050

