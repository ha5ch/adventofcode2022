from os import path
import pathlib


def read_file(filename="data.txt") -> list[str]:
    filepath = path.join(pathlib.Path(__file__).parent.absolute(), filename)
    with open(filepath, 'r') as f:
        return f.read().splitlines()


def is_unique(value: str) -> bool:
    return len(set(value)) == len(value)


def detect(data: str, marker_len=4) -> tuple[str, int]:
    for i in range(marker_len, len(data)+1):
        part = data[i-marker_len:i]
        if is_unique(part):
            return part, i


if __name__ == '__main__':
    # data = read_file("example.txt")
    data = read_file()
    for sequence in data:
        p1 = detect(sequence)
        print("part1", p1)
    for sequence in data:
        p2 = detect(sequence, 14)
        print("part2", p2)
