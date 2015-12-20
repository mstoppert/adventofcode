file = open("input.txt")
input = file.readline()

def first_star(input):
    level = 0

    for char in input:
        if char == "(":
           level += 1
        elif char == ")":
            level -=1
        else:
            continue

    print level

def second_star(input):
    level = 0
    position = 1

    for char in input:
        if char == "(":
            level += 1
        elif char == ")":
            level -=1
        else:
            continue

        if level == -1:
            print position
            break

        position += 1

first_star(input)
second_star(input)
