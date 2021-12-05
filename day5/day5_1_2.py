class LineSegment:

    def __init__(self, f, t):
        self.f = [int(i) for i in f]
        self.t = [int(i) for i in t]

    def draw_hor_ver(self, board):
        if not self.is_hor_or_ver():
            return

        x_from = min(self.f[0], self.t[0])
        x_to = max(self.f[0], self.t[0])
        
        y_from = min(self.f[1], self.t[1])
        y_to = max(self.f[1], self.t[1])

        for x in range(x_from, x_to + 1):
            for y in range(y_from, y_to + 1):
                board[x][y] += 1
    
    def draw_diag(self, board):
        x_up = self.f[0] < self.t[0]
        y_rl = self.f[1] < self.t[1]

        x = self.f[0]
        y = self.f[1]

        while True:
            # print(self, x, y)
            board[x][y] += 1

            if x == self.t[0] and y == self.t[1]:
                break
            if x_up:
                x += 1
            else:
                x -= 1
            
            if y_rl:
                y += 1
            else:
                y -= 1
    
    def is_hor_or_ver(self):
        return self.f[0] == self.t[0] or self.f[1] == self.t[1]

    def __repr__(self) -> str:
        return f'{self.f} -> {self.t}'

def max_x(data):
    return max([i.f[0] for i in data] + [i.t[0] for i in data])

def max_y(data):
    return max([i.f[1] for i in data] + [i.t[1] for i in data])

def load_input():
    res = []
    with open('./day5/input.txt', 'r') as f:
        for line in f.readlines():
            points = line.rstrip().split(' -> ')

            res.append(LineSegment(points[0].split(','), points[1].split(',')))
    
    size_x = max_x(res)
    size_y = max_y(res)

    return res, [[0] * (size_y + 1) for i in range(size_x + 1 )]

def calc_score(board):
    total = 0
    for i in board:
        for j in i:
            if j > 1:
                total += 1
    return total

data, board = load_input()

for i in data:
    i.draw_hor_ver(board)

print(calc_score(board))

# p2
data, board = load_input()
for i in data:
    if i.is_hor_or_ver():
        i.draw_hor_ver(board)
    else:
        i.draw_diag(board)

print(calc_score(board))
