def read_file(filename="data.txt"):
    with open(filename, 'r') as f:
        return f.read().splitlines()


def part1():
    data = [[int(x) for x in range.split('-')]
            for pairs in read_file() for range in pairs.split(",")]
    pairs = [data[i:i+2] for i in range(0, len(data), 2)]

    return sum([1 for a, b in pairs if a[0] <= b[0] <= a[1] >= b[1] or b[0] <= a[0] <= b[1] >= a[1]])


def part2():
    data = [[int(x) for x in range.split('-')]
            for pairs in read_file() for range in pairs.split(",")]
    pairs = [data[i:i+2] for i in range(0, len(data), 2)]

    return sum([1 for a, b in pairs if a[0] <= b[0] <= a[1] or b[0] <= a[0] <= b[1]])


print("part1", part1())
print("part2", part2())
