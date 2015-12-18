import re
import itertools
from collections import defaultdict

def calc_distance(path, distances):
    return sum(
        distances[path[i]][path[i + 1]]
        for i in range(len(path) - 1)
    )


def first_star():
    cities = distances.keys()

    path = min(
        itertools.permutations(cities),
        key=lambda path: calc_distance(path, distances)
    )

    return calc_distance(path, distances)


def second_star():
    cities = distances.keys()

    path = max(
        itertools.permutations(cities),
        key=lambda path: calc_distance(path, distances)
    )

    return calc_distance(path, distances)


file = open("input.txt")
distances = defaultdict(dict)

for line in file.readlines():
    a, b, distance = re.match(r'(\w+) to (\w+) = (\d+)', line).groups()

    distance = int(distance)

    distances[a][b] = distance
    distances[b][a] = distance


print first_star()
print second_star()