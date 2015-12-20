from itertools import combinations

file = open("input.txt")

def read_containers(file):
    containers = []
    for line in file.readlines():
        containers.append(int(line))

    # test input
    # return [20, 15, 10, 5, 5]
    return containers

def first_star(available_containers, eggnog_to_store):
    possible_combinations = []
    for r in range(1, len(available_containers) + 1):
        for combination in combinations(available_containers, r):
            if sum(combination) == eggnog_to_store:
                possible_combinations.append(combination)

    print len(possible_combinations)
    print possible_combinations

    return possible_combinations


def second_star(possible_combinations):
    min_containers = min([len(c) for c in possible_combinations])

    count_combinations = 0
    for combination in possible_combinations:
        if len(combination) == min_containers:
            count_combinations += 1

    print min_containers
    print count_combinations

available_containers = read_containers(file)
# test input
# eggnog_to_store = 25
eggnog_to_store = 150

possible_combinations = first_star(available_containers, eggnog_to_store)
second_star(possible_combinations)