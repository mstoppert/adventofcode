import re

file = open("input.txt")

def test_state(i, state, r, a, w):
    print "-" * 10
    print i
    print "%s testing %s" % (r, a)
    if state[r][a] == w:
        print "correct"
    else:
        print "wanted %r %r" % (a, w)
        print "   got %r %r" % (a, state[r][a])

def read_reindeers(file):
    reindeer = {}

    # lines = [
    #     "Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.",
    #     "Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds."
    # ]

    for line in file.readlines():
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
            "tick": reindeers[r]["fly_time"],
            "dist": reindeers[r]["fly_dist"],
            "points": 0
        }
    else:
        state = states[r]["state"]
        dist = states[r]["dist"]
        tick = states[r]["tick"] - 1
        points = states[r]["points"]

        if tick == 0:
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
            "dist": dist,
            "points": points
        }


reindeers = read_reindeers(file)
reindeers_state = {}
for i in range(1, 2503 + 1):
    for r in reindeers:
        reindeers_state[r] = calculate_step(r, reindeers, reindeers_state)

    # second star ranking
    current_lead = max([reindeers_state[rs]["dist"] for rs in reindeers_state])
    for r in reindeers:
        if reindeers_state[r]["dist"] == current_lead:
            reindeers_state[r]["points"] += 1

    # After one second, Comet has gone 14 km, while Dancer has gone 16 km.
    # After ten seconds, Comet has gone 140 km, while Dancer has gone 160 km.
    # On the eleventh second, Comet begins resting (staying at 140 km),
    # and Dancer continues on for a total distance of 176 km.
    # On the 12th second, both reindeer are resting.
    # They continue to rest until the 138th second,
    # when Comet flies for another ten seconds. On the 174th second, Dancer flies for another 11 seconds.
    #
    # In this example, after the 1000th second, both reindeer are resting,
    # and Comet is in the lead at 1120 km
    # (poor Dancer has only gotten 1056 km by that point).
    # So, in this situation, Comet would win (if the race ended at 1000 seconds).

    # if i == 1:
    #     test_state(i, reindeers_state, "Comet", "dist", 14)
    #     test_state(i, reindeers_state, "Dancer", "dist", 16)
    # elif i == 10:
    #     test_state(i, reindeers_state, "Comet", "dist", 140)
    #     test_state(i, reindeers_state, "Dancer", "dist", 160)
    # elif i == 11:
    #     test_state(i, reindeers_state, "Comet", "dist", 140)
    #     test_state(i, reindeers_state, "Comet", "state", "rest")
    #
    #     test_state(i, reindeers_state, "Dancer", "dist", 176)
    # elif i == 12:
    #     test_state(i, reindeers_state, "Comet", "state", "rest")
    #     test_state(i, reindeers_state, "Dancer", "state", "rest")
    # elif i == 138:
    #     pass
    #     #print i
    #     #print reindeers_state
    #     #print reindeers_state["Comet"]["state"] == "fly"
    #     #print reindeers_state["Comet"]["tick"] == 10
    #
    #     #print reindeers_state["Dancer"]["state"] == "fly"
    # elif i == 174:
    #     test_state(i, reindeers_state, "Dancer", "tick", 11)
    # elif i == 1000:
    #     test_state(i, reindeers_state, "Comet", "state", "rest")
    #     test_state(i, reindeers_state, "Comet", "dist", 1120)
    #
    #     test_state(i, reindeers_state, "Dancer", "state", "rest")
    #     test_state(i, reindeers_state, "Dancer", "dist", 1056)

print "-" * 20

# first star
print max([reindeers_state[rs]["dist"] for rs in reindeers_state])
# second star
print max([reindeers_state[rs]["points"] for rs in reindeers_state])