def load_input():
    res = []
    with open('./day6/sample.txt', 'r') as f:
        return [int(i) for i in f.readline().rstrip().split(',')]

fish = load_input()
for i in range(0, 80):
    n_fish = []
    for i in fish:
        if i == 0:
            n_fish.append(8)
            n_fish.append(6)
        else:
            n_fish.append(i - 1)
    fish = n_fish.copy()

print(len(fish))