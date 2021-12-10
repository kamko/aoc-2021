def load_input():
    with open('./day10/input.txt', 'r') as f:
        return [i.rstrip() for i in f.readlines()]

brace_score = {
    ')' : 3,
    ']': 57,
    '}':  1197,
    '>': 25137,
    None: 0
}

def is_open(brace):
    return brace in ['(', '[', '{', '<']

def is_close(brace):
    return brace in [')', ']', '}', '>']

def oposite(brace):
    if brace == '(':
        return ')'
    if brace == '[':
        return ']'
    if brace == '{':
        return '}'
    if brace == '<':
        return '>'
    
    if brace == ')':
        return '('
    if brace == ']':
        return '['
    if brace == '}':
        return '{'
    if brace == '>':
        return '<'

def check_row(row):
    closing = []

    for c in row:
        if is_open(c):
            closing.append(oposite(c))
        if is_close(c):            
            if c != closing.pop():
                return c

            if len(closing) == 0:
                return None

    return None

if __name__ == '__main__':
    print(sum((brace_score[check_row(i)] for i in load_input())))
