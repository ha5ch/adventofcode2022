import re
from os import path
import pathlib

DEBUG_PRINT = False

PATTERN_CRATES = re.compile(r'(\[\w\]|\s\s\s)\s?')
PATTERN_INSTRUCTIONS = re.compile(r'move (\d{1,2}) from (\d) to (\d)')

EMPTY = '   '


def read_file(filename="data.txt") -> list[str]:
    filepath = path.join(pathlib.Path(__file__).parent.absolute(), filename)
    with open(filepath, 'r') as f:
        return f.read().splitlines()


def split_data(data: list[str]) -> tuple[list[int], list[list[str]], list[tuple[str]]]:
    split = data.index('')
    columns = [int(x) for x in list(data[split-1]) if x.isdigit()]
    stack = [PATTERN_CRATES.findall(line) for line in data[:split-1]]
    instructions = [PATTERN_INSTRUCTIONS.findall(
        line) for line in data[split+1:]]
    return columns, stack, instructions


def print_stack(stack: list[list[str]], columns: list[int]) -> None:
    for line in stack:
        for col in line:
            print(col, end="")
        print()
    print(columns)
    print('-'*3*len(columns))


def gen_output(stack: list[list[str]], columns: list[int]) -> str:
    result = []
    for i in range(len(columns)):
        for j in range(len(stack)):
            if stack[j][i] != EMPTY:
                result.append(stack[j][i])
                break
    return ''.join([c[1] for c in result])


def get_item_from(stack: list[list[str]], column: int) -> str:
    for line in stack:
        if line[column] == EMPTY:
            continue
        item = line[column]
        line[column] = EMPTY
        return item


def move_item_to(stack: list[list[str]], item: str, column: int, width=9) -> None:
    moved = False
    for i in range(len(stack)-1, -1, -1):
        if stack[i][column] == EMPTY:
            stack[i][column] = item
            moved = True
            break
    if not moved:
        stack.insert(0, [EMPTY] * width)
        stack[0][column] = item
    while stack[0] == [EMPTY] * width:
        stack.pop(0)


def part1(debug=DEBUG_PRINT) -> tuple[str, list[list[str]]]:
    data = read_file()
    columns, stack, instructions = split_data(data)
    if debug: print_stack(stack, columns)

    for instruction in instructions:
        amount = int(instruction[0][0])
        now = int(instruction[0][1])-1
        after = int(instruction[0][2])-1
        for _ in range(amount):
            item = get_item_from(stack, now)
            if not item: raise ValueError('item is None but should contain value')
            move_item_to(stack, item, after, len(columns))
        if debug: print_stack(stack, columns)

    return gen_output(stack, columns), stack.copy()


def part2(debug=DEBUG_PRINT) -> tuple[str, list[list[str]]]:
    data = read_file()
    columns, stack, instructions = split_data(data)
    if debug:
        print_stack(stack, columns)

    for instruction in instructions:
        amount = int(instruction[0][0])
        now = int(instruction[0][1])-1
        after = int(instruction[0][2])-1
        tmp = []
        for _ in range(amount):
            item = get_item_from(stack, now)
            if not item: raise ValueError('item is None but should contain value')
            tmp.insert(0, item)
        for item in tmp: 
            move_item_to(stack, item, after, len(columns))
        if debug: print_stack(stack, columns)

    return gen_output(stack, columns), stack.copy()


if __name__ == "__main__":
    if not DEBUG_PRINT:
        data = read_file()
        columns, stack, instructions = split_data(data)
        print_stack(stack, columns)

    p1, stack_p1 = part1()
    if not DEBUG_PRINT:
        print_stack(stack_p1, columns)

    print("part1", p1)

    print("="*9*3)

    if not DEBUG_PRINT:
        data = read_file()
        columns, stack, instructions = split_data(data)
        print_stack(stack, columns)

    p2, stack_p2 = part2()
    if not DEBUG_PRINT:
        print_stack(stack_p2, columns)

    print("part2", p2)
