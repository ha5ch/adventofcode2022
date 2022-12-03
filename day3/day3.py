def read_file(filename="data.txt"):
    with open(filename, 'r') as f:
        return f.read().splitlines()


def get_priority(part):
    return ord(part) % 96 if part.islower() else ord(part) % 64+26


def part1():
    rucksacks = read_file()

    sum = 0
    for rucksack in rucksacks:
        mid = len(rucksack)//2
        for part in rucksack[:mid]:
            if part in rucksack[mid:]:
                sum += get_priority(part)
                break
    return sum


def part2():
    rucksacks = read_file()
    
    sum = 0
    for i in range(len(rucksacks)//3):
        start, end = i*3, i*3+3
        group = sorted(rucksacks[start:end], key=len)
        for part in group[0]:
            if part in group[1] and part in group[2]:
                sum += get_priority(part)
                break

    return sum


print(part1())
print(part2())
