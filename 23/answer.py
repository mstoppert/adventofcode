file = open('input.txt')

instructions = []

for line in file.readlines():
    instructions.append(line.replace(',', '').strip().split(' '))

regs = {
    'a': 0,
    'b': 0
}

ptr = 0
while True:
    if ptr not in range(len(instructions)):
        break

    instr = instructions[ptr]
    inst, r = instr[0], instr[1]
    
    di = 1

    if inst == 'inc':
        regs[r] += 1
    elif inst == 'tpl':
        regs[r] *= 3
    elif inst == 'hlf':
        regs[r] //= 2
    elif inst == 'jie':
        offset = instr[2]
        if regs[r] % 2 == 0: di = int(offset)
    elif inst == 'jio':
        offset = instr[2]
        if regs[r] == 1: di = int(offset)
    elif inst == 'jmp':
        di = int(r)

    ptr += di

print regs