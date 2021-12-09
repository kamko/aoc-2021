def load_input():
    with open('./day9/input.txt', 'r') as f:
        return [[j for j in i.rstrip()] for i in f.readlines()]

def is_valid_point(map, point, seen):
    if point[0] < 0:
        return False
    if point[1] < 0:
        return False
    if point[0] >= len(map):
        return False
    if point[1] >= len(map[0]):
        return False
    if map[point[0]][point[1]] == '9':
        return False
    if point in seen:
        return False
    
    return True

def points_around(map, point, seen):
    res = []

    if is_valid_point(map, (point[0] + 1, point[1]), seen):
        res.append((point[0] + 1, point[1]))
    if is_valid_point(map, (point[0], point[1] + 1), seen):
        res.append((point[0], point[1] + 1))
    if is_valid_point(map, (point[0] - 1, point[1]), seen):
        res.append((point[0] - 1, point[1]))
    if is_valid_point(map, (point[0], point[1] - 1), seen):
        res.append((point[0], point[1] - 1))

    return res

seen = set()
def bfs(map, start):
    if start in seen or map[start[0]][start[1]] == '9':
        return -1
    
    basin = []
    todo = [start]

    while len(todo) > 0:
        point = todo.pop(0)
        if point in seen:
            continue

        seen.add(point)
        basin.append(point)

        todo = todo + points_around(map, point, seen)  

    return len(basin)

map = load_input()

results = []

for i, row in enumerate(map):
    for j, _ in enumerate(row):
        results.append(bfs(map, (i, j)))

top_three = list(sorted(results))[-3:]

print(top_three[0] * top_three[1] * top_three[2])