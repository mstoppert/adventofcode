import json

file = open("input.json")
json_input = json.loads(file.read())


def sum_numbers(input, ignore_red):
    total = 0

    if isinstance(input, int):
        total += input
    elif isinstance(input, dict):
        if 'red' not in input.values() or ignore_red == False:
            for item in input.values():
                total += sum_numbers(item, ignore_red)
    elif isinstance(input, list):
            for item in input:
                total += sum_numbers(item, ignore_red)

    return total

# first star
print sum_numbers(json_input, False)
# second star
print sum_numbers(json_input, True)