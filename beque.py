import re
import sys

if len(sys.argv) < 2:
    program = sys.stdin.read()
else:
    with open(sys.argv[1], 'r') as file:
        program = file.read()

program = re.sub(r'#.*\n', '', program)
program = program.split()

print(repr(program))
