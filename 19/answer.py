import re
from random import shuffle

file = open("input.txt")
# file = open("input_first_star_test.txt")
# file = open("input_second_star_test.txt")

def replacemenent_and_molecule(file):
    replacements = []
    molecule = ""

    for line in file.readlines():
        line = line.strip()

        if re.search(r'=>', line):
            token, replacement = line.split(' => ')
            replacements.append((token, replacement))
        else:
            if line != "":
                molecule = line

    return replacements, molecule


def do_replacements(replacement, molecule):
    molecules = set()
    i = molecule.find(replacement[0])
    if i != -1:
        molecules.add(molecule.replace(replacement[0], replacement[1], 1))
        for replacement_str in do_replacements(replacement, molecule[i + 1:]):
            molecules.add(molecule[:i + 1] + replacement_str)

    return molecules


def replacements_for_molecule(replacemenents, molecule):
    return {molecules for replacement in replacemenents for molecules in do_replacements(replacement, molecule)}


def invert_replacements(replacements):
    new_replacements = []
    for r in replacements:
        new_replacements.append((r[1], r[0]))

    return new_replacements

def first_star():
    replacemenents, molecule = replacemenent_and_molecule(file)
    return len(replacements_for_molecule(replacemenents, molecule))


def second_star():
    '''
    First approach worked for the testcase but didn't complete for the real input.

    Fortunately a reddit user simplified the problem:
    https://www.reddit.com/r/adventofcode/comments/3xflz8/day_19_solutions/cy4etju

    The equation for finding the solution is:
    count(tokens) - count(Rn and Ar) - 2*count(Y) - 1
    '''

    replacements, molecule = replacemenent_and_molecule(file)

    reg = sum(el.isupper() for el in molecule)
    parens = molecule.count('Rn') + molecule.count('Ar')
    comma = molecule.count('Y')

    return reg - parens - 2 * comma - 1

# print first_star()
print second_star()