with open('./day2/input.txt', 'r') as f:
    x = [(j[0], int(j[1])) for j in [i.split() for i in f.readlines()]]

depth = 0
forward = 0
aim = 0

for d, v in x:
    if d == 'down':
        aim += v
    elif d == 'up':
        aim -= v
    elif d == 'forward':
        forward += v
        depth += aim * v
        depth = max(0, depth)

print(f'depth: {depth} and forward: {forward}')
print(depth * forward)