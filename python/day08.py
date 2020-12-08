from typing import List, Dict
from copy import deepcopy


def get_inputs(fn: str = "toy") -> Dict:
    with open(f"../inputs/day08/{fn}inputs.txt", "r") as f:
        inpt = [x.strip().split() for x in f.readlines()]
    return {(i + 1): (x, int(y)) for i, (x, y) in enumerate(inpt)}


def boot(ins: Dict) -> int:
    accumulator = 0
    ln = 1
    while True:
        # print(ln, ins.get(ln, False), accumulator)
        if not ins.get(ln, False):
            return accumulator
        if ins.get(ln, False)[0] == "nop":
            ins.pop(ln)
            ln += 1
        elif ins.get(ln, False)[0] == "jmp":
            k = ins[ln][1]
            ins.pop(ln)
            # print("Jump : ", ln, "->", ln + k)
            ln += k
        else:
            accumulator += ins[ln][1]
            # print("Acc : ", accumulator)
            ins.pop(ln)
            ln += 1


def boot2(ins: Dict) -> int:
    maxk = set(ins.keys())

    repair = []
    for i, (instr, val) in ins.items():
        if instr == "jmp":
            k = deepcopy(ins)

            k[i] = ("nop", val)
            repair.append(k)
    for i, (instr, val) in ins.items():
        if instr == "nop":
            k = deepcopy(ins)
            k[i] = ("jmp", val)
            repair.append(k)

    iii = []
    for t in repair:
        accumulator = 0
        ln = 1
        while True:
            if not t.get(ln, False):
                iii.append(False if (ln in maxk) else accumulator)
                break
            if t.get(ln, False)[0] == "nop":
                t.pop(ln)
                ln += 1
            elif t.get(ln, False)[0] == "jmp":
                k = ins[ln][1]
                t.pop(ln)
                ln += k
            else:
                accumulator += ins[ln][1]
                t.pop(ln)
                ln += 1
    return max(iii)


if __name__ == "__main__":
    toy = get_inputs()
    print(boot(toy))
    # assert boot(toy) == 5

    puzzle = get_inputs("puzzle")
    # print("Part 1: ", boot(puzzle))
    toy = get_inputs()
    print(boot2(puzzle))
