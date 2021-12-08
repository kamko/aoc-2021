def load_input():
    with open('./day8/input.txt', 'r') as f:
        return [i.replace('| ', '').rstrip().split(' ') for i in f.readlines()]

def count_of_len(row, ln):
    return sum(1 for i in row if len(i) == ln)

total = 0
for i in load_input():
    output = i[-4:]
    total += count_of_len(output, ln=2) # 1
    total += count_of_len(output, ln=4) # 4
    total += count_of_len(output, ln=3) # 7
    total += count_of_len(output, ln=7) # 8

print(total)