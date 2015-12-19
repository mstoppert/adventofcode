import re

def increment_string(s):
    pos = ord(s[-1])

    upper_limit = 122
    loop_to = 97

    new_pos = pos + 1 if pos + 1 <= upper_limit else loop_to

    if pos + 1 <= upper_limit:
        return s[:-1] + chr(new_pos)
    else:
        return increment_string(s[:-1]) + chr(new_pos)


def does_contain_invalid_letters(s):
    return re.search("[iol]", s) is not None


def does_contain_three_letters_one_apart(s):
    found_three_letters_one_apart = False
    for i in range(0, len(s) -2):
        triple = s[i:i+3]

        p1 = ord(triple[0])
        p2 = ord(triple[1])
        p3 = ord(triple[2])

        if p2 - p1 == 1 and p3 - p1 == 2:
            found_three_letters_one_apart = True
            break

    return found_three_letters_one_apart


def does_contain_two_pairs(s):
    found_two_pairs = False
    count_pairs = 0
    pass_next = False

    for i in range(0, len(s) -1):
        if pass_next:
            pass_next = False
            continue

        double = s[i:i+2]

        if double[0] == double[1]:
            count_pairs += 1
            pass_next = True
            if count_pairs == 2:
                found_two_pairs = True
                break

    return found_two_pairs


def is_valid_password(s):
    if does_contain_invalid_letters(s):
        return False

    if not does_contain_three_letters_one_apart(s):
        return False

    if not does_contain_two_pairs(s):
        return False

    return True

# first star
input = "hxbxwxba"

# second star
input = "hxbxxyzz"

while True:
    input = increment_string(input)
    if is_valid_password(input):
        break

print input