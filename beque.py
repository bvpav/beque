import collections
import re
import sys

if len(sys.argv) < 2:
    program = sys.stdin.read()
else:
    with open(sys.argv[1], 'r') as file:
        program = file.read()

program = re.sub(r'#.*\n', '', program)
program = program.split()

deque = collections.deque()


def push(left: bool, value):
    if left:
        deque.appendleft(value)
    else:
        deque.append(value)


def pop(left: bool):
    if left:
        return deque.popleft()
    else:
        return deque.pop()


funcs = {}


def func(f_or_name):
    def inner(f, name):
        funcs[name] = f
        return f

    if callable(f_or_name):
        return inner(f_or_name, f_or_name.__name__)

    return lambda f: inner(f, f_or_name)


@func('+')
def add(left):
    a = pop(left)
    b = pop(left)
    push(left, a + b)


@func('-')
def sub(left):
    a = pop(left)
    b = pop(left)
    push(left, b - a)


@func('print')
def print_func(left):
    value = pop(left)
    print(value)


ip = 0
while ip < len(program):
    print(deque)
    instruction = program[ip]
    if instruction.startswith('.'):
        left = True
        instruction = instruction[1:]
    elif instruction.endswith('.'):
        left = False
        instruction = instruction[:-1]
    else:
        raise RuntimeError(f'missing position at {ip}: {instruction!r}')

    print(f'{ip=} {instruction=} {left=}')

    if instruction.isnumeric():
        push(left, int(instruction))
    elif instruction in funcs:
        funcs[instruction](left)
    else:
        raise NameError(instruction)

    ip += 1
