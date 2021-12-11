def load_input():
    with open('./day11/input.txt', 'r') as f:
        return [[int(j) for j in i.rstrip()] for i in f.readlines()]

world = load_input()

def in_bounds(point):
    if point[0] >= 0 and point[0] < 10 and point[1] >= 0 and point[1] < 10:
        return True

    return False

def increase_around(world, point):
    changes = [
        (1, 0),
        (0, 1),
        (-1, 0),
        (0, -1),
        (1, 1),
        (1, -1),
        (-1, 1),
        (-1, -1)
    ]

    res = False
    for i,j in changes:
        change_point = (point[0] + i, point[1] + j)
        if in_bounds(change_point):
            world[change_point[0]][change_point[1]] += 1
            if world[change_point[0]][change_point[1]] > 9:
                res = True

    return res

def run_step(world):
    flashed = set()

    finished = False
    first_run = True
    while not finished:
        found_some = False
        for i, row in enumerate(world):
            for j, _ in enumerate(row):
                if first_run:
                    world[i][j] += 1

                if world[i][j] > 9 and (i,j) not in flashed:
                    if increase_around(world, (i, j)):
                        found_some = True
                    flashed.add((i,j))
        if found_some:
            finished = False
        else:
            finished = True
        first_run = False
    
    for i,j in flashed:
        world[i][j] = 0

    return len(flashed)

def pprint(world):
    for r in world:
        print('\t'.join([str(i) for i in r]))
    
    print('----')

def p1():
    world = load_input()
    total = 0
    for i in range(100):
        total += run_step(world)

    print(f'After 100 rounds: {total}')

p1()

# --
def p2():
    world = load_input()
    step = 0
    while True:
        step += 1
        flashed = run_step(world)
        if flashed == 100:
            break
    print(f'All flashed after {step} steps.')

p2()