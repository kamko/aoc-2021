def load_input():
    with open('./day7/input.txt', 'r') as f:
        return [int(i) for i in f.readline().rstrip().split(',')]

from statistics import median

data = load_input()
target = int(median(data))
cost = sum((abs(target - i) for i in data))

print(f'target: {target} - cost: {cost}')