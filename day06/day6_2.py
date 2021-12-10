def load_input():
    with open('./day6/input.txt', 'r') as f:
        return [int(i) for i in f.readline().rstrip().split(',')]

fish = [0] * 9

for i in load_input():
    fish[i] += 1

for i in range(256):
    n_fish = [0] * 9

    finished = fish[0]
    for j in range(1, 9):
        n_fish[j - 1] = fish[j]
    
    n_fish[8] += finished
    n_fish[6] += finished

    fish = n_fish

print(sum(fish))