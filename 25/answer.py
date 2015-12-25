row = 2978
col = 3083

first_code = 20151125


def next_code(current_code):
    return (current_code * 252533) % 33554393


def code_count(row, column):
    return sum(range(row + column - 1)) + column

code_number = code_count(row, col)

code = first_code
for i in range(code_number - 1):
    code = next_code(code)

print code