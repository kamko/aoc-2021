def load_input():
    with open('./day15/input.txt', 'r') as f:
        return [[int(j) for j in i.rstrip()] for i in f.readlines()]

map = load_input()

start = (0,0)
x_size = len(map[0])
y_size = len(map)

def in_bounds(point):
    if point[0] >= 0 and point[0] < 5*len(map[0]) and point[1] >= 0 and point[1] < 5*len(map):
        return True

    return False

from collections import defaultdict
from heapq import heappush, heappop

seen = set()
distances = defaultdict(lambda: 99999999)

heap = [(0, start)]
distances[start] = 0

def dst_fun(map, point):
    x = point[0] % (x_size)
    y = point[1] % (y_size)

    x_penalty = int(point[0] / (x_size))
    y_penalty = int(point[1] / (y_size))

    res = map[x][y] + x_penalty + y_penalty
    res = ((res - 1) % 9) + 1

    return res


while len(heap) > 0:
    dst, take = heappop(heap)
    
    if take in seen:
        continue

    seen.add(take)

    for x,y in [(take[0] + i, take[1] + j) for i,j in [(1,0), (0,1), (-1, 0), (0, -1)] if in_bounds((take[0] + i, take[1] + j))]:
        if (x,y) in seen:
            continue
        alt_dst = dst + dst_fun(map, (x,y))
        distances[(x,y)] = min(distances[(x,y)], alt_dst)
        heappush(heap, (distances[(x,y)], (x,y)))


print(distances[((x_size) * 5 - 1, (y_size) * 5 - 1)])
