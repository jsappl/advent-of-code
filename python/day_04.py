"""Day 4: Passport Processing"""


def read_from(file_: str) -> list:
    """Generate list of passports as dictionaries from file."""
    passports = []
    passport = dict()  # init
    with open(file_, "r") as f:
        for line in f.readlines():
            if not line[:-1]:  # omit \n character
                passports.append(passport)
                passport = dict()  # reset
            else:
                for field in line[:-1].split(" "):
                    key, _, value = field.partition(":")
                    passport[key] = value
    return passports


def valid(passport: dict) -> bool:
    """Return true if all required fields are in passport."""
    required = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])
    return required.issubset(set(passport.keys()))


def valid_fields_of(passport: dict) -> bool:
    """Check every field's values according to these rules."""
    pass_check = True
    if not valid(passport):
        return False
    for key, value in passport.items():
        if key == "byr" and pass_check:
            pass_check = 1919 < int(value) < 2003
        if key == "iyr" and pass_check:
            pass_check = 2009 < int(value) < 2021
        if key == "eyr" and pass_check:
            pass_check = 2019 < int(value) < 2031
        if key == "hgt" and pass_check:
            if value[-2:] == "cm":
                pass_check = 149 < int(value[:-2]) < 194
            elif value[-2:] == "in":
                pass_check = 58 < int(value[:-2]) < 77
            else:
                pass_check = False
        if key == "hcl" and pass_check:
            pass_check = value[0] == "#" and len(value) == 7 and set(value[1:]).issubset(
                {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"})
        if key == "ecl" and pass_check:
            pass_check = value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        if key == "pid" and pass_check:
            pass_check = len(value) == 9 and value.isdigit()
    return pass_check


def main():
    # CAVE: Add bottom empty line otherwise read_from won't work.
    file_ = "./assets/data/04.txt"
    passports = read_from(file_)

    # part one
    n_valid = 0
    for passport in passports:
        n_valid += 1 if valid(passport) else 0
    print(f"Found {n_valid} valid passports.")

    # part two
    n_valid = 0
    for passport in passports:
        n_valid += 1 if valid_fields_of(passport) else 0
    print(f"Found {n_valid} valid passports with only valid fields.")


if __name__ == "__main__":
    main()
