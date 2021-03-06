import collections
import functools
import re
import sys

if len(sys.argv) < 2:
    program = sys.stdin.read()
else:
    with open(sys.argv[1], 'r') as file:
        program = file.read()

program = re.sub(r'#.*\n', '', program)
program = program.split()


def push(is_left: bool, value):
    if is_left:
        deque.appendleft(value)
    else:
        deque.append(value)


def pop(is_left: bool):
    if is_left:
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


def special_case(f):
    @functools.wraps(f)
    def error(is_left):
        raise RuntimeError(f'special case {f.__name__!r} not handled')
    return error


@func('+')
def add(is_left):
    a = pop(is_left)
    b = pop(is_left)
    push(is_left, a + b)


@func('-')
def sub(is_left):
    b = pop(is_left)
    a = pop(is_left)
    push(is_left, a - b)


@func('++')
def inc(is_left):
    a = pop(is_left)
    push(is_left, a + 1)


@func('--')
def dec(is_left):
    a = pop(is_left)
    push(is_left, a - 1)


@func('=')
def eq(is_left):
    b = pop(is_left)
    a = pop(is_left)
    push(is_left, 1 if a == b else 0)


@func('!=')
def neq(is_left):
    b = pop(is_left)
    a = pop(is_left)
    push(is_left, 1 if a != b else 0)



@func('<')
def lt(is_left):
    b = pop(is_left)
    a = pop(is_left)
    push(is_left, 1 if a < b else 0)


@func('>')
def gt(is_left):
    b = pop(is_left)
    a = pop(is_left)
    push(is_left, 1 if a > b else 0)


@func('<=')
def lte(is_left):
    b = pop(is_left)
    a = pop(is_left)
    push(is_left, 1 if a <= b else 0)


@func('>=')
def gte(is_left):
    b = pop(is_left)
    a = pop(is_left)
    push(is_left, 1 if a >= b else 0)


@func
def dup(is_left):
    val = pop(is_left)
    push(is_left, val)
    push(is_left, val)


@func('print')
def print_func(is_left):
    value = pop(is_left)
    print(value)


@func
def argv(is_left):
    proc_argv = sys.argv[1:]
    push(is_left, int(proc_argv[pop(is_left)]))


@func
def movee(is_left):
    value = pop(is_left)
    push(not is_left, value)


@func
@special_case
def jmp(is_left):
    pass


@func
@special_case
def jmpif(is_left):
    pass


labels = {}
for i, instruction in enumerate(program):
    if instruction.endswith(':'):
        label = instruction[:-1]
        if label in funcs:
            raise RuntimeError(
                    f'label {label!r} at position {i} shadows builtin name {label!r}')
        labels[label] = i + 1

deque = collections.deque()

ip = 0
while ip < len(program):
    instruction = program[ip]
    if instruction.startswith('.'):
        is_left = True
        instruction = instruction[1:]
    elif instruction.endswith('.'):
        is_left = False
        instruction = instruction[:-1]
    elif instruction.endswith(':'):
        ip += 1
        continue
    else:
        raise RuntimeError(f'missing direction at {ip}: {instruction!r}')

    print(f'{ip=} {instruction=} {is_left=} {deque=}', file=sys.stderr)

    if instruction.isnumeric():
        push(is_left, int(instruction))
    elif instruction == 'jmp':
        ip = pop(is_left)
        continue
    elif instruction == 'jmpif':
        label = pop(is_left)
        condition = pop(is_left)
        if condition != 0:
            ip = label
            continue
    elif instruction in funcs:
        funcs[instruction](is_left)
    else:
        push(is_left, labels[instruction])

    ip += 1
