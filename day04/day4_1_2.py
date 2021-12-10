class Board:

    def __init__(self, board):
        self.board = [[(int(q), False) for q in j] for j in [i.split() for i in board]]
        self.last_seen_num = None

    def draw(self, num):
        self.last_seen_num = num
        for i in range(0, 5):
            for j in range(0, 5):
                if self.board[i][j][0] == num:
                    self.board[i][j] = (num, True)
                    
                    if self.is_win_row(i) or self.is_win_col(j):
                        return True
                    else:
                        return False
    
    def is_win_row(self, row):
        for i in range(0, 5):
            if self.board[row][i][1] == False:
                return False

        return True

    def is_win_col(self, col):
        for i in range(0, 5):
            if self.board[i][col][1] == False:
                return False

        return True
    
    def unmarked_sum(self):
        total = 0
        for i in range(0, 5):
            for j in range(0, 5):
                if self.board[i][j][1] == False:
                    total += self.board[i][j][0]
        
        return total
    
    def score(self):
        return self.unmarked_sum() * self.last_seen_num

    def pprint(self):
        for i in range(0, 5):
            print('\t\t'.join(str(j[1]) for j in self.board[i]))
        print('---')

def load_input():
    with open('./day4/input.txt', 'r') as f:
        draw_order = [int(i) for i in f.readline().split(',')]

        x = [i.rstrip() for i in f.readlines() if i != '\n']

        boards = []
        for i in range(0, len(x), 5):
            boards.append(Board(x[i:i+5]))
    return draw_order, boards

def draw():
    draw_order, boards = load_input()
    for i in draw_order:
        for b in boards:
            res = b.draw(i)
            if res == True:
                return b, i

winning_board, last_number = draw()

print(winning_board.unmarked_sum() * last_number)

# part 2


def draw_2():
    draw_order, boards = load_input()

    skip = []
    for i in draw_order:
        for j in range(0, len(boards)):
            if j in skip:
                continue

            res = boards[j].draw(i)
            if res == True:
                skip.append(j)
    
    return boards[skip[-1]]

last_board = draw_2()
print(last_board.score())