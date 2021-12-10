with open('./day1/input.txt', 'r') as f:
    x = [int(i) for i in f.readlines()]

total = 0
for i in range(1, len(x)):
    if x[i] > x[i - 1]:
        print(x[i],' ', x[i-1])
        total += 1

print(total)
