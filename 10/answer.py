def capture_sequence(string):
    current_char = None

    list = []
    sublist = []
    for char in string:
        if current_char != char:
            current_char = char
            if len(sublist) > 0:
                list.append(sublist)

            sublist = []

        sublist.append(char)

    list.append(sublist)

    return list


def convert_sequence(list):
    sequence = ""

    for sublist in list:
        length = str(len(sublist))
        char = sublist.pop()

        sequence += length
        sequence += char

    return sequence


def run(input, times):
    seq = input

    for i in range(1, times + 1):
        list = capture_sequence(seq)
        seq = convert_sequence(list)

    print len(seq)


def first_star():
    run("1113122113", 40)


def second_star():
    run("1113122113", 50)


first_star()
second_star()