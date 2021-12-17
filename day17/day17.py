import re

def load_input():
    with open('./day17/input.txt', 'r') as f:
        res = re.search('target area: x=(-?\d+)\.\.(-?\d+), y=(-?\d+)..(-?\d+)', f.readline().rstrip())
        return (int(res.group(1)), int(res.group(2))), (int(res.group(3)), int(res.group(4)))
        

def x_pos(velocity, steps):
    x_pos = 0
    for i in range(steps):
        x_pos += velocity
        if velocity > 0:
            velocity -= 1
        elif velocity < 0:
            velocity += 1
    
    return x_pos

def y_pos(velocity, steps):
    y_pos = 0
    for i in range(steps):
        y_pos += velocity
        velocity -= 1
    
    return y_pos

def is_past_target(x_target, y_target, point):
    return (point[0] > x_target[1] and point[0] > x_target[0]) or (point[1] < y_target[0] and point[1] < y_target[1])
    

def is_in_target_area(x_target, y_target, point):
    return (x_target[0] <= point[0] <= x_target[1]) and (y_target[0] <= point[1] <= y_target[1])

x_target, y_target = load_input()

def run():
    points = []
    for x_vel in range(x_target[1] + 1):
        for y_vel in range(400, -400, -1):
            i = 0
            max_y = -99999999
            while True:
                point = (x_pos(x_vel, i), y_pos(y_vel, i))
                max_y = max(point[1], max_y)
                i += 1
                if is_in_target_area(x_target, y_target, point):
                    # print(i, max_y, x_vel, y_vel, point)
                    points.append((max_y, point))
                    break
                if is_past_target(x_target, y_target, point):
                    break
    return points

res = run()
print(f'max_y = {max(i[0] for i in res)}')
print(f'total_choices = {len(res)}')