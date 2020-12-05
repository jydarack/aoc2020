from typing import List, Dict
import re


def get_inputs(type: str) -> List[Dict]:
    with open(f"../inputs/day04/{type}.txt", "r") as f:
        inpt = f.read()

    inpt = inpt.split("\n\n")  ## get all info on each passport
    for i, ppt in enumerate(inpt):
        out = {}
        for k in re.split("[\s\n]", ppt):  ## split on either space or new line
            ## Build the dictionary
            print(k)
            ky, vlue = k.split(":")
            out[ky] = vlue
        inpt[i] = out
    return inpt


def check_req(passport: Dict) -> bool:
    all_req = [
        "byr",
        "iyr",
        "eyr",
        "hgt",
        "hcl",
        "ecl",
        "pid",
        # "cid",
    ]
    return all(passport.get(x, False) for x in all_req)


def minmax(val, mi, ma):
    return (val >= mi) & (val <= ma)


def form_height(val):
    if (val[-2:] in ["in", "cm"]) & val[:-2].isnumeric():
        if val[-2:] == "cm":
            return minmax(int(val[:-2]), 150, 193)
        else:
            return minmax(int(val[:-2]), 59, 76)
    else:
        return False


def hair(val):
    return True if re.match("#[0-9a-f]{6}", val) else False


def check_details(passport: Dict) -> bool:
    check = []
    if passport.get("byr", False):
        k = passport.get("byr", False)
        check.append(minmax(int(k), 1920, 2002) & (len(k) == 4))
    if passport.get("iyr", False):
        k = passport.get("iyr", False)
        check.append(minmax(int(k), 2010, 2020) & (len(k) == 4))
    if passport.get("eyr", False):
        k = passport.get("eyr", False)
        check.append(minmax(int(k), 2020, 2030) & (len(k) == 4))
    if passport.get("hgt", False):
        k = passport.get("hgt", False)
        check.append(form_height(k))
    if passport.get("hcl", False):
        k = passport.get("hcl", False)
        check.append(hair(k))
    if passport.get("ecl", False):
        k = passport.get("ecl", False)
        check.append(k in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"])
    if passport.get("pid", False):
        k = passport.get("pid", False)
        check.append(k.isnumeric() & (len(k) == 9))

    return all(check)


if __name__ == "__main__":
    toy = get_inputs("toyinputs")
    assert len(toy) == 4
    assert list(check_req(x) for x in toy) == [True, False, True, False]

    puzzle = get_inputs("puzzleinputs")
    print("Correct passwords: ", sum(check_req(x) for x in puzzle))  # 237

    assert minmax(2002, 1920, 2002)
    assert minmax(2003, 1920, 2002) == False
    assert form_height("60in")
    assert form_height("190cm")
    assert not form_height("190in")
    assert not form_height("190")
    assert hair("#123abc")
    assert not hair("#123abz")
    assert not hair("123abc")

    valid = get_inputs("correctpassports")
    k = [check_details(x) for x in valid if check_req(x)]
    assert all(k)

    valid = get_inputs("incorrectpassports")
    k = [check_details(x) for x in valid if check_req(x)]
    assert not all(k)

    print(
        "Passports with correct info: ",
        sum(check_details(x) for x in puzzle if check_req(x)),
    )  ## 172
