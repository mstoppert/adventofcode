file = open("input.txt")


def read_about_sues(file):
    what_i_remember_about_sues = {}
    for line in file.readlines():
        sue, prop_str = line.strip().split(":", 1)
        sue = int(sue.replace("Sue ", ""))

        properties = {}
        for prop in prop_str.split(","):
            property, amount = prop.strip().split(": ")
            properties[property] = int(amount)

        what_i_remember_about_sues[sue] = properties

    return what_i_remember_about_sues

def first_star(what_sue_has_got):
    sues = read_about_sues(file)
    for sue in sues.keys():
        for prop, v in what_sue_has_got.items():
            if prop in sues[sue] and sues[sue][prop] != v:
                del sues[sue]
                break

    return sues

def second_star(what_sue_has_got):
    sues = read_about_sues(file)
    for sue in sues.keys():
        for prop, v in what_sue_has_got.items():
            if prop in sues[sue]:
                if prop == "cats" or prop == "trees":
                    if sues[sue][prop] <= v:
                        del sues[sue]
                        break
                elif prop == "pomeranians" or prop == "goldfish":
                    if sues[sue][prop] >= v:
                        del sues[sue]
                        break
                else:
                     if sues[sue][prop] != v:
                        del sues[sue]
                        break

    return sues


what_sue_has_got = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1
}

# print first_star(what_sue_has_got)
print second_star(what_sue_has_got)