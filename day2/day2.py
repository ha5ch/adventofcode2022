
shapes = {
    'rock': 1,
    'paper': 2,
    'scissor': 3,
}

outcomes = {
    'win': 6,
    'draw': 3,
    'lose': 0,
}

# A => Rock
# B => Paper
# C => Scissor

table1 = {
    # X => Rock
    'A X': shapes['rock']+outcomes['draw'],  # Rock    - Rock => DRAW
    'B X': shapes['rock']+outcomes['lose'],  # Paper   - Rock => LOSE
    'C X': shapes['rock']+outcomes['win'],   # Scissor - Rock => WIN
    # Y => Paper
    'A Y': shapes['paper']+outcomes['win'],   # Rock    - Paper => WIN
    'B Y': shapes['paper']+outcomes['draw'],  # Paper   - Paper => DRAW
    'C Y': shapes['paper']+outcomes['lose'],  # Scissor - Paper => LOSE
    # Z => Scissor
    'A Z': shapes['scissor']+outcomes['lose'],  # Rock    - Scissor => LOSE
    'B Z': shapes['scissor']+outcomes['win'],   # Paper   - Scissor => WIN
    'C Z': shapes['scissor']+outcomes['draw'],  # Scissor - Scissor => DRAW
}

table2 = {
    # X => Lose
    'A X': outcomes['lose']+shapes['scissor'],  # Rock    - Scissor => LOSE
    'B X': outcomes['lose']+shapes['rock'],     # Paper   - Rock    => LOSE
    'C X': outcomes['lose']+shapes['paper'],    # Scissor - Paper   => LOSE
    # Y => Draw
    'A Y': outcomes['draw']+shapes['rock'],     # Rock    - Rock    => DRAW
    'B Y': outcomes['draw']+shapes['paper'],    # Paper   - Paper   => DRAW
    'C Y': outcomes['draw']+shapes['scissor'],  # Scissor - Scissor => DRAW
    # Z => Win
    'A Z': outcomes['win']+shapes['paper'],    # Rock    - Paper   => WIN
    'B Z': outcomes['win']+shapes['scissor'],  # Paper   - Scissor => WIN
    'C Z': outcomes['win']+shapes['rock'],     # Scissor - Rock    => WIN
}


def read_file(filename="data.txt"):
    with open(filename, 'r') as f:
        return f.read().splitlines()


if __name__ == '__main__':
    data = read_file()
    points1 = [table1[x] for x in data]
    print('Round one:', sum(points1))
    points2 = [table2[x] for x in data]
    print('Round two:', sum(points2))
