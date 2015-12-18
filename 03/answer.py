file = open("input.txt")
input = file.readline()

def key(x, y):
    return "%d,%d" % (x, y)


def deliver_present(houses, key):
    if key in houses:
        houses[key] += 1
    else:
        houses[key] = 1

    return houses


def adjust_position(char, x, y):
    if char == "^":
        x -= 1
    elif char == "v":
        x += 1
    elif char == ">":
        y += 1
    elif char == "<":
        y -= 1

    return x, y

def first_star(input):
    houses = {}
    x = 0
    y = 0

    for char in input:

        houses = deliver_present(houses, key(x, y))
        x, y = adjust_position(char, x, y)

    houses = deliver_present(houses, key(x, y))

    print len(houses)


def second_star(input):

    houses = {}

    x_santa = 0
    y_santa = 0

    x_robot = 0
    y_robot = 0

    count = 1

    for char in input:

        if count % 2 == 1:
            houses = deliver_present(houses, key(x_santa, y_santa))
            x_santa, y_santa = adjust_position(char, x_santa, y_santa)
        else:
            houses = deliver_present(houses, key(x_robot, y_robot))
            x_robot, y_robot = adjust_position(char, x_robot, y_robot)

        count += 1


    houses = deliver_present(houses, key(x_santa, y_santa))
    houses = deliver_present(houses, key(x_robot, y_robot))

    print houses
    print len(houses)


#first_star(input)
second_star(input)