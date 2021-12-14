def load_input():
    with open('./day14/input.txt', 'r') as f:
        template = f.readline().rstrip()
        
        f.readline()

        transforms = {x.split(' -> ')[0]: x.split(' -> ')[1].rstrip() for x in f.readlines()}

        return template, transforms


template, transforms = load_input()

def grow(template, transforms):
    res = ''
    for pair in (template[i-1:i+1] for i in range(1, len(template))):
        res += pair[0] + transforms[pair]

    return res + template[-1]

for i in range(10):
    template = grow(template, transforms)
    print(f'after step: {i+1} - len: {len(template)}')

from collections import Counter

counter = Counter(template)
mc = counter.most_common()

max = mc[0][1]
min = mc[-1][1]

print(max - min)
