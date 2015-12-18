import numpy

file = open("input.txt")
lights = numpy.zeros((1000,1000), 'int')

def split_instruction(line):
    split = line.split(' ')

    if "turn on" in line or "turn off" in line:
        instruction = "%s_%s" % (split[0], split[1])
        first_pair = [int(x) for x in split[2].split(",")]
        second_pair = [int(x) for x in split[4].split(",")]

    elif "toggle" in line:
        instruction = split[0]
        first_pair = [int(x) for x in split[1].split(",")]
        second_pair = [int(x) for x in split[3].split(",")]

    return instruction, first_pair, second_pair


def apply_instruction_first_star(instruction, first_pair, second_pair):
    for x in xrange(first_pair[0], second_pair[0] + 1):
        for y in xrange(first_pair[1], second_pair[1] + 1):
            if instruction == "turn_on":
                lights[x][y] = 1
            elif instruction == "turn_off":
                lights[x][y] = 0
            elif instruction == "toggle":
                if lights[x][y] == 1:
                    lights[x][y] = 0
                else:
                    lights[x][y] = 1

def apply_instruction_second_star(instruction, first_pair, second_pair):
    for x in xrange(first_pair[0], second_pair[0] + 1):
        for y in xrange(first_pair[1], second_pair[1] + 1):
            if instruction == "turn_on":
                lights[x][y] += 1
            elif instruction == "turn_off":
                lights[x][y] -= 1
                if(lights[x][y] < 0):
                    lights[x][y] = 0
            elif instruction == "toggle":
                lights[x][y] += 2

# apply instructions
for line in file.readlines():
    instruction, first_pair, second_pair = split_instruction(line)
    #apply_instruction_first_star(instruction, first_pair, second_pair)
    apply_instruction_second_star(instruction, first_pair, second_pair)

# count lights
sum = 0
for x in lights:
    sum += x.sum()

print sum