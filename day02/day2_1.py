with open('./day2/input.txt', 'r') as f:
    x = [(j[0], int(j[1])) for j in [i.split() for i in f.readlines()]]

depth = 0
forward = 0
for d, v in x:
    if d == 'down':
        depth += v
    elif d == 'up':
        depth -= v
        if depth <= 0:
            depth = 0
    elif d == 'forward':
        forward += v

print(f'depth: {depth} and forward: {forward}')
print(depth * forward)