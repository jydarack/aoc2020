from typing import List


def gold_coins(inputs: List[int]) -> int:
    """
    Doing accounting for the Elves
    """
    vals = {2020 - x for x in inputs}
    out = 1
    for v in vals:
        if v in inpt:
            out *= v
    return out


def gold_coins2(inputs: List[int]) -> int:
    """
    Doing accounting for the Elves, now with 3 transactions
    """
    vals = {2020 - x - y for i, x in enumerate(inputs[:-1]) for y in inputs[i + 1 :]}
    out = 1
    for v in vals:
        if v in inpt:
            out *= v
    return out


def get_inputs(fn: str) -> List:
    with open(fn, "r") as f:
        inpt = [int(l.strip()) for l in f.readlines()]
    return inpt


if __name__ == "__main__":
    ## Dev Day 1 Pt 1
    inpt = get_inputs("toyinputs.txt")
    assert len(inpt) == 6
    assert all([type(x) == int for x in inpt])
    gc = gold_coins(inpt)
    assert gc == 514579

    ## Actual Day 1 Pt 1
    inpt = get_inputs("puzzleinputs.txt")
    gc = gold_coins(inpt)
    print(gc)
    ## Actual Day 1 Pt 2
    inpt = get_inputs("puzzleinputs.txt")
    gc = gold_coins2(inpt)
    print(gc)
