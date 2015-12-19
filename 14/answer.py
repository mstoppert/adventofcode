import re

file = open("input.txt")

def read_reindeers(file):
    reindeer = {}

    lines = [
        "Comet can fly 1 km/s for 1 seconds, but then must rest for 1 seconds.",
        "Dancer can fly 2 km/s for 1 seconds, but then must rest for 1 seconds."
    ]

    for line in lines:#file.readlines():
        split = line.strip()
        matches = re.match(r'(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.', line).groups()

        reindeer[matches[0]] = {
            "fly_time": int(matches[2]),
            "fly_dist": int(matches[1]),
            "rest_time": int(matches[3])
        }

    return reindeer

def toggle_state(s):
    if s == "fly":
        return "rest"
    else:
        return "fly"

def calculate_step(r, reindeers, states):
    if r not in states:
        return {
            "state": "fly",
            "tick": reindeers[r]["fly_time"] - 1,
            "dist": reindeers[r]["fly_dist"]
        }
    else:
        state = states[r]["state"]
        dist = states[r]["dist"]
        tick = states[r]["tick"] - 1

        if tick <= 0:
            state = toggle_state(state)
            if state == "fly":
                tick = reindeers[r]["fly_time"]
            else:
                tick = reindeers[r]["rest_time"]

        if state == "fly":
            dist += reindeers[r]["fly_dist"]

        return {
            "state": state,
            "tick": tick,
            "dist": dist
        }


reindeers = read_reindeers(file)
reindeers_state = {}
for i in range(1, 2503 + 1):
    for r in reindeers:
        reindeers_state[r] = calculate_step(r, reindeers, reindeers_state)

print reindeers_state
print max([reindeers_state[rs]["dist"] for rs in reindeers_state])