from day10_1 import is_open, is_close, oposite

def load_input():
    with open('./day10/input.txt', 'r') as f:
        return [i.rstrip() for i in f.readlines()]

def check_row(row):
    closing = []

    for c in row:
        if is_open(c):
            closing.append(oposite(c))
        if is_close(c):
            if c != closing.pop():
                return []

    return list(reversed(closing))

brace_score = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

scores = []
for r in load_input():
    score = 0
    for b in check_row(r):
        score *= 5
        score += brace_score[b]
    
    if score != 0:
        scores.append(score)

from statistics import median

print(median(scores))