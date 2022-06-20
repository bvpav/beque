import re
import sys

if len(sys.argv) < 2:
    program = sys.stdin.read()
else:
    with open(sys.argv[1], 'r') as file:
        program = file.read()

program = re.sub(r'#.*\n', '', program)
program = program.split()

ip = 0
while ip < len(program):
    instruction = program[ip]
    if instruction.startswith('.'):
        left = False
        instruction = instruction[1:]
    elif instruction.endswith('.'):
        left = True
        instruction = instruction[:-1]
    print(f'{ip=} {instruction=} {left=}')
    ip += 1
