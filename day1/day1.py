def read_file(filename="data.txt"):
    with open(filename, 'r') as f:
        return [l.strip() for l in f.readlines()]


def calculate_calories(data):
    sums = []
    sum = 0
    # print(data)
    for d in data:
        if d != '':
            sum += int(d)
        else:
            sums.append(sum)
            sum = 0
    
    sums.sort(reverse=True)
    return sums

if __name__ == '__main__':
    calories = calculate_calories(read_file())
    print(calories[0]) # solution 1
    print(sum(calories[0:3])) # solution 2