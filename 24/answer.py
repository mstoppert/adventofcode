from functools import reduce
from itertools import combinations
from operator import mul

file = open("input.txt")
pkgs = [int(x.strip()) for x in file.readlines()]


def solve(num_groups):
    weight_goal = sum(pkgs) // num_groups
    for i in range(len(pkgs)):
        qes = [reduce(mul, c) for c in combinations(pkgs, i)
              if sum(c) == weight_goal]
        if qes:
            return min(qes)

# first star
print(solve(3))

# second star
print(solve(4))