def load_input():
    with open('./day7/input.txt', 'r') as f:
        return [int(i) for i in f.readline().rstrip().split(',')]

data = load_input()

cost_table = [sum(range(0, i)) for i in range(max(data)+2)]

def dst(f, t):
    if f > t:
        return cost_table[f - t + 1]
    else:
        return cost_table[t - f + 1]

left = min(data)
right = max(data)

print(left, right)

positions = [i for i in range(left, right + 1)]
def calc_to(target, cutoff):
    score = 0
    for i in data:
        score += dst(f=i, t=target)

        if score > cutoff:
            return None

    return score

cutoff = 99999999999
for i in positions:
    res = calc_to(i, cutoff=cutoff)
    if res is not None:
        cutoff = res
    
print(cutoff)