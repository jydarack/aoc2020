from typing import List, Tuple
from collections import Counter


def parse_policy(policy: str) -> Tuple:
    """
    Parsing the input string into its components
    """
    minmax, letter, pwd = policy.split()
    min, max = [int(x) for x in minmax.split("-")]
    letter = letter.replace(":", "")
    return (min, max, letter, pwd)


def raw_inputs(fn: str) -> List:
    """
    Extracting the raw input files
    """
    with open(fn, "r") as f:
        inpt = [parse_policy(x.strip()) for x in f.readlines()]

    return inpt


def check_policy(pol: Tuple) -> bool:
    """
    Check if 1 given password follows its policy
    """
    min, max, letter, pwd = pol
    ctr = Counter(pwd)[letter]
    if (ctr >= min) & (ctr <= max):
        return True
    return False


def check_policy2(pol: Tuple) -> bool:
    """
    Check if 1 given password follows its policy
    """
    min, max, letter, pwd = pol

    if (pwd[min - 1] == letter) ^ (pwd[max - 1] == letter):
        return True
    return False


if __name__ == "__main__":
    # Toy exemple and check
    k = raw_inputs("toypass.txt")
    assert [check_policy(x) for x in k] == [True, False, True]
    assert [check_policy2(x) for x in k] == [True, False, False]

    # Part 1
    k = raw_inputs("puzzlepass.txt")
    print("Correct passwords (pt 1): ", sum([check_policy(x) for x in k]))

    # part 2
    print("Correct passwords (pt 2): ", sum([check_policy2(x) for x in k]))
