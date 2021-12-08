def load_input():
    with open('./day8/input.txt', 'r') as f:
        data = [i.replace('| ', '').rstrip().split(' ') for i in f.readlines()]
        return [[''.join(sorted(j)) for j in i] for i in data]

def count_of_len(row, ln):
    return sum(1 for i in row if len(i) == ln)

def find_code(row, ln):
    for i in row:
        if len(i) == ln:
            return i

def find_containing(row, chars, eight):
    for i in row:
        if i == eight:
            continue
        x = set(i)
        if set(chars).issubset(x):
            return i

def srt(val):
    return ''.join(sorted(val))

total = 0
for i in load_input():
    input = i[:-4]
    output = i[-4:]

    one = find_code(row=input, ln=2)
    four = find_code(row=input, ln=4)
    seven = find_code(row=input, ln=3)
    eight = find_code(row=input, ln=7)

    a = ''.join(set(seven).difference(set(one)))

    nine = find_containing(row=input, eight=eight, chars=four + a)

    g = ''.join(set(nine).difference(set(four + a)))
    e = ''.join(set(eight).difference(set(nine)))

    zero = find_containing(row=input, eight=eight, chars=seven + g + e)
    d = ''.join(set(eight).difference(set(zero)))
    b = ''.join(set(zero).difference(set(seven + e + g)))

    six = find_containing(row=input, eight=eight, chars=a + b + d + e + g)
    
    c = ''.join(set(one).difference(set(six)))
    f = ''.join(set(one).difference(set(c)))

    three = seven + d + g

    five = set(six)
    five.remove(e)

    two = set(three)
    two.remove(f)
    two.add(e)
    # ---


    calc_map = {
        ''.join(sorted(zero)) : '0',
        ''.join(sorted(one)) : '1',
        ''.join(sorted(two)) : '2',
        ''.join(sorted(three)) : '3',
        ''.join(sorted(four)) : '4',
        ''.join(sorted(five)) : '5',
        ''.join(sorted(six)) : '6',
        ''.join(sorted(seven)) : '7',
        ''.join(sorted(eight)) : '8',
        ''.join(sorted(nine)) : '9',
    }

    res = int(''.join([calc_map[i] for i in output]))
    total += res

print(total)