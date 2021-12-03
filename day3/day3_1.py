with open('./day3/input.txt', 'r') as f:
    x = [list(i.rstrip()) for i in f.readlines()]

cols = []
for i in range(0, len(x[0])):
    col = [int(j[i]) for j in x]
    col_sum = sum(col)

    cols += [col_sum]

res_gamma = ''

for i in cols:
    if i >= len(x) / 2:
        res_gamma += '1'
    else:
        res_gamma += '0'

res_epsilon = res_gamma.replace('0', '2').replace('1', '0').replace('2', '1')

print(f'gamma={res_gamma} , epsilon={res_epsilon}')


res_gamma_dec = int(res_gamma, 2)
res_epsilon_dec = int(res_epsilon, 2)

print(res_gamma_dec * res_epsilon_dec)