from copy import deepcopy

# file = open("input_test.txt")
file = open("input.txt")


def read_configuration(file):
    grid = []
    for line in file.readlines():
        grid.append(list(line.strip()))

    return grid


def neighbours(grid, me_x, me_y):
    grid_len = len(grid) - 1
    neighbours = []

    for x in range(me_x - 1, me_x + 2):
        for y in range(me_y - 1, me_y + 2):
            if x == me_x and y == me_y:
                continue

            neighbour = 0
            if 0 <= x <= grid_len and 0 <= y <= grid_len:
                if grid[x][y] == '#':
                    neighbour = 1

            neighbours.append(neighbour)

    return sum(neighbours)

def is_on(str):
    if str == '#':
        return True

    return False


def step(old_grid, lights_stuck):
    new_grid = deepcopy(old_grid)

    for x, v in enumerate(old_grid):
        for y, v2 in enumerate(v):

            n = neighbours(old_grid, x, y)
            light_on = is_on(old_grid[x][y])

            if light_on:
                if n == 2 or n == 3:
                    new_grid[x][y] = '#'
                else:
                    new_grid[x][y] = '.'
            else:
                if n == 3:
                    new_grid[x][y] = '#'
                else:
                    new_grid[x][y] = '.'

            # second star
            if lights_stuck and x in [0, len(old_grid) - 1] and y in [0, len(old_grid) - 1]:
                new_grid[x][y] = '#'

    return new_grid


def print_grid(grid):
    for x, v in enumerate(grid):
        print v

    print ""


def lights_on(grid):
    on = 0

    for row, v in enumerate(grid):
        for cell, v2 in enumerate(v):
            if v2 == '#':
                on += 1

    return on


def run(lights_stuck):
    steps = 100
    grid = read_configuration(file)
    for i in range(1, steps + 1):
        grid = step(grid, lights_stuck)

    print lights_on(grid)


def first_star():
    run(False)


def second_star():
    run(True)


# first_star()
second_star()