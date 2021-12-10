def load_input():
    with open('./day9/input.txt', 'r') as f:
        return [[j for j in i.rstrip()] for i in f.readlines()]

def is_low_point(map, x, y):
    y_bound = len(map[0])
    x_bound = len(map)

    val = map[x][y]
    if (x+1) < x_bound and val >= map[x+1][y]:
        return False
    if (y+1) < y_bound and val >= map[x][y+1]:
        return False
    if (x-1) >= 0 and val >= map[x-1][y]:
        return False
    if (y-1) >= 0 and val >= map[x][y-1]:
        return False
    
    return True

low_points = []

data = load_input()
for i, row in enumerate(data):
    for j, _ in enumerate(row):
        if is_low_point(data, i, j):
            low_points.append(data[i][j])

print(sum((int(i) for i in low_points)) + len(low_points))
