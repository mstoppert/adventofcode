file = open("input.txt")

def encode_line(line):
    return (
        len(line)
        + line.count('"')
        + line.count('\\')
        + 2  # count quotes around string
    )

char_count_literal = 0
char_count_memory = 0
char_count_encoded = 0

for line in file.readlines():

    line = line.strip()

    char_count_literal += len(line)
    char_count_memory += len(eval(line))

    char_count_encoded += encode_line(line)

# first_star
print char_count_literal - char_count_memory
# second_star
print char_count_encoded - char_count_literal
