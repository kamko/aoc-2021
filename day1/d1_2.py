with open('./day1/input.txt', 'r') as f:
    x = [int(i) for i in f.readlines()]

total = 0

def window_sum(vals, begin):
    if begin + 2 >= len(vals):
        return None
    
    return vals[begin] + vals[begin + 1] + vals[begin + 2]

p_sum = window_sum(x, 0)
for i in range(1, len(x) - 2):
    n_sum = window_sum(x, i)

    if n_sum > p_sum:
        total += 1
    
    p_sum = n_sum

print(total)

