from collections import defaultdict


def first_star():
    presents = 29000000
    elf_multiplicator = 10
    houses = defaultdict(int)

    for elf in range(1, presents):
        for house in range(elf, 1000000, elf):
            houses[house] += elf * elf_multiplicator

        if houses[elf] >= presents:
            return elf


def second_star():
    presents = 29000000
    elf_multiplicator = 11
    houses = defaultdict(int)

    for elf in range(1, presents):
        for house in range(elf, min(elf * 50 + 1, 10000000), elf):
            houses[house] += elf * elf_multiplicator

        if houses[elf] >= presents:
            return elf


# print first_star()
print second_star()