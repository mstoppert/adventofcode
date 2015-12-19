import itertools

file = open("input.txt")

def guest_list(file, include_myself):
    guests  = {}

    if include_myself:
        guests["myself"] = {}

    for line in file.readlines():
        split = line.strip().split(' ')

        guest = split[0]
        other_guest = split[-1][:-1]
        happiness = int(split[3])

        if split[2] == 'lose':
            happiness *= - 1

        if guest not in guests:
            guests[guest] = {}
            if include_myself:
                guests["myself"][guest] = 0
                guests[guest]["myself"] = 0

        guests[guest][other_guest] = happiness

    return guests


def calculate_happiness(seating, guests):
    happiness = []
    count_guests = len(seating)
    for i in range(count_guests):
        guest = seating[i]
        previous_guest = seating[i - 1]
        next_guest = seating[ (i + 1) % count_guests ]
        happiness.append(guests[guest][previous_guest] + guests[guest][next_guest])

    return happiness

def calculate_best_seating(guests):
    return max(
        [sum(calculate_happiness(seating, guests)) for seating in itertools.permutations(guests)]
    )

# first star
print calculate_best_seating(guest_list(file, False))
# second star
print calculate_best_seating(guest_list(file, True))
