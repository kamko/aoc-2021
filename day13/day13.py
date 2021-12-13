def load_input():
    with open('./day13/input.txt', 'r') as f:
        dots = set()
        commands = []

        line = f.readline()
        while line != '\n':
            dots.add(tuple(reversed([int(i) for i in line.rstrip().split(',')])))
            line = f.readline()

        for l in f.readlines():
            cmd = l.rstrip().split(' ')[2]
            commands.append((cmd.split('=')[0], int(cmd.split('=')[1])))
        
        return dots, commands

def do_fold(dots, fold):
    res = set(dots)
    for i in dots:
        if fold[0] == 'x':
            if i[1] > fold[1]:
                new = (i[0], i[1] - (i[1] - fold[1])*2)
                res.add(new)
                res.remove(i)
        elif fold[0] == 'y':
            if i[0] > fold[1]:
                new = (i[0] - (i[0] - fold[1])*2, i[1])
                res.add(new)
                res.remove(i)

    return res

def p1():
    dots, commands = load_input()
    print(len(do_fold(dots, commands[0])))

p1()

# ---

def p2():
    dots, commands = load_input()

    for i in commands:
        dots = do_fold(dots, i)

    my = max((i[0] for i in dots)) + 1
    mx = max((i[1] for i in dots)) + 1

    for i in range(my):
        for j in range(mx):
            if (i,j) in dots:
                print('#', end='')
            else:
                print('.', end='')
        print('')
    
p2()