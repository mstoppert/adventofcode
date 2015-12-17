file = open("input.txt")

def calculate_wrap(side1, side2, side3):
    min_side = min(side1, side2, side3)

    return 2 * side1 + 2 * side2 + 2 * side3 + min_side

def calculate_ribbon(l, w, h, side1, side2, side3):
    min_side = min(side1, side2, side3)

    if min_side == side1:
        perimeter = 2 * l + 2 * w
    elif min_side == side2:
        perimeter = 2 * w + 2 * h
    elif min_side == side3:
        perimeter = 2 * l + 2 * h

    return perimeter + l * w * h

wrap = 0
ribbon = 0

for line in file.readlines():
    l, w, h = [int(x) for x in line.split("x")]

    side1 = l * w
    side2 = w * h
    side3 = h * l

    wrap += calculate_wrap(side1, side2, side3)
    ribbon += calculate_ribbon(l, w, h, side1, side2, side3)

print wrap
print ribbon