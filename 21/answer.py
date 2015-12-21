from itertools import combinations


def fight(player):
    boss = [103, 9, 2]
    while True:
        boss[0] -= max(player[1] - boss[2], 1)
        if boss[0] <= 0:
            return True

        player[0] -= max(boss[1] - player[2], 1)
        if player[0] <= 0:
            return False


weapons = {
    (8, 4, 0),
    (10, 5, 0),
    (25, 6, 0),
    (40, 7, 0),
    (74, 8, 0)
}

armor = {
    (0, 0, 0),
    (13, 0, 1),
    (31, 0, 2),
    (53, 0, 3),
    (75, 0, 4),
    (102, 0, 5),
}

rings = {
    (0, 0, 0),
    (0, 0, 0),
    (25, 1, 0),
    (50, 2, 0),
    (100, 3, 0),
    (20, 0, 1),
    (40, 0, 2),
    (80, 0, 3),
}

wins = []
losses = []
for weapon_cost, weapon_damage, _ in weapons:
    for armor_cost, __, armor_armor in armor:
        for ring1, ring2 in combinations(rings, 2):
            if fight([100, weapon_damage + ring1[1] + ring2[1], armor_armor + ring1[2] + ring2[2]]):
                wins.append(weapon_cost + armor_cost + ring1[0] + ring2[0])
            else:
                losses.append(weapon_cost + armor_cost + ring1[0] + ring2[0])

# first star
print min(wins)
# second star
print max(losses)
