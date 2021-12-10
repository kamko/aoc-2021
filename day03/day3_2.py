with open('./day3/input.txt', 'r') as f:
    x = [list(i.rstrip()) for i in f.readlines()]

def gamma(data):
    cols = []
    for i in range(0, len(data[0])):
        col = [int(j[i]) for j in data]
        col_sum = sum(col)

        cols += [col_sum]

    res_gamma = ''

    for i in cols:
        if i >= len(data) / 2:
            res_gamma += '1'
        else:
            res_gamma += '0'

    return res_gamma

def calc(ones=True):
    y = x.copy()

    i = 0
    while len(y) > 1:
        res_gamma = gamma(y)
        yy = []
        for c in y:
            if (int(res_gamma[i]) == int(c[i])) == ones:
                yy.append(c)
        
        y = yy
        i += 1

    return int(''.join(y[0]), 2)

oxygen = calc(ones=True)
co2 = calc(ones=False)

print(f'oxygen: {oxygen} co2: {co2}')
print(oxygen * co2)
