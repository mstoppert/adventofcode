file = open("input.txt")

vowels = "aeiou"
not_in = ["ab", "cd", "pq", "xy"]


def is_nice_string_first_star(string):
    nice_string = True

    if nice_string is not False:
        for naughty in not_in:
            if naughty in string:
                nice_string = False
                break;

    if nice_string is not False:
        vowel_count = 0
        for char in string:
            if char in vowels:
                vowel_count += 1

        if vowel_count < 3:
            nice_string = False

    if nice_string is not False:
        length = len(string) - 1
        found_double_char = False
        for index, char in enumerate(string):
            if index+1 <= length:
                if char == string[index+1]:
                    found_double_char = True
                    break;

        if not found_double_char:
            nice_string = False

    return nice_string


def is_nice_string_second_star(string):
    nice_string = True

    if nice_string is not False:
        recurring_substring = False
        length = len(string)
        for index, char in enumerate(string):
            if index+1 <= length:
                substring = string[index:index+2]
                if len(substring) == 2 and string.count(substring) >= 2:
                    recurring_substring = True
                    break

        if not recurring_substring:
            nice_string = False

    if nice_string is not False:
        length = len(string) - 1
        double_char_with_char_between = False
        for index, char in enumerate(string):
            if index+3 <= length:
                substring = string[index:index+3]
                if substring[0] == substring[2]:
                    double_char_with_char_between = True
                    break;

        if not double_char_with_char_between:
            nice_string = False

    return nice_string


nice_strings_first_star = 0
nice_strings_second_star = 0

for line in file.readlines():
    if is_nice_string_first_star(line):
        nice_strings_first_star += 1

    if is_nice_string_second_star(line):
        nice_strings_second_star += 1

print nice_strings_first_star
print nice_strings_second_star