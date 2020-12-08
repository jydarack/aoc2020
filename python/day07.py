from typing import DefaultDict, List, Tuple, Set
from collections import defaultdict
import re


def get_inputs(fn: str = "toy") -> List[str]:
    with open(f"../inputs/day07/{fn}inputs.txt", "r") as f:
        inpt = f.readlines()

    return inpt


def get_policy(inpt: List) -> DefaultDict:
    pat = "(\d*)[\s]?(\w*\s\w*) bag[.*]*"
    out = defaultdict()
    for detail in inpt:
        res = list(re.findall(pat, detail))
        res.reverse()
        source = res.pop()[1]
        out[source] = defaultdict(int)
        for pair in res:
            n, col = pair
            if n:
                out[source][col] = int(n)

    return out


def get_contained(policies: DefaultDict, bag: str) -> int:
    out = 0
    if not policies[bag].keys():
        return 1
    for k in policies[bag].keys():
        out += policies[bag][k] * get_contained(policies, k)

    return out


if __name__ == "__main__":
    toy = get_inputs()
    assert len(toy) == 9

    my_bag = "shiny gold"
    pol = get_policy(toy)
    print(get_contained(pol, my_bag))
    # assert get_sol(toy, my_bag) == 4

    # puzzle = get_inputs("puzzle")
    # print("sol ", get_sol(puzzle, my_bag))  # 287

    # print(get_sol2(toy, my_bag))
