file = open("input.txt")
wires = {}

def resolve_wire(wire):

    if wires[wire]["result"] is not None:
        return wires[wire]["result"]

    if wires[wire]["left_argument"] is not None and type(wires[wire]["left_argument"]) is not int:
        wires[wire]["left_argument"] = resolve_wire(wires[wire]["left_argument"])

    if wires[wire]["right_argument"] is not None and type(wires[wire]["right_argument"]) is not int:
        wires[wire]["right_argument"] = resolve_wire(wires[wire]["right_argument"])
    
    if wires[wire]["operator"] == "AND":
        wires[wire]["result"] = wires[wire]["left_argument"] & wires[wire]["right_argument"]
    elif wires[wire]["operator"] == "OR":
        wires[wire]["result"] = wires[wire]["left_argument"] | wires[wire]["right_argument"]
    elif wires[wire]["operator"] == "LSHIFT":
        wires[wire]["result"] = wires[wire]["left_argument"] << wires[wire]["right_argument"]
    elif wires[wire]["operator"] == "RSHIFT":
        wires[wire]["result"] = wires[wire]["left_argument"] >> wires[wire]["right_argument"]
    elif wires[wire]["operator"] == "NOT":
        wires[wire]["result"] = ~ wires[wire]["right_argument"]
    else:
        wires[wire]["result"] = wires[wire]["left_argument"]


    return wires[wire]["result"]


for line in file.readlines():
    sides = line.split(" -> ")
    left_side = sides[0].split(" ")
    right_side = sides[1].strip("\n")

    instruction = {
        "original": line.strip("\n"),
        "result": None,
        "left_argument": None,
        "right_argument": None,
        "operator": None
    }

    if len(left_side) == 3:
        instruction["left_argument"] = left_side[0]
        instruction["operator"] = left_side[1]
        instruction["right_argument"] = left_side[2]
    elif len(left_side) == 2:
        instruction["operator"] = left_side[0]
        instruction["right_argument"] = left_side[1]
    elif len(left_side) == 1:
        instruction["left_argument"] = left_side[0]

    if instruction["left_argument"] is not None and instruction["left_argument"].isdigit():
        instruction["left_argument"] = int(instruction["left_argument"])

    if instruction["right_argument"] is not None and instruction["right_argument"].isdigit():
        instruction["right_argument"] = int(instruction["right_argument"])

    wires[right_side] = instruction

# first_star
#print resolve_wire('a')

# second_star
wires['b']['result'] = 46065
print resolve_wire('a')