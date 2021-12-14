from collections import Counter


def load_input():
    with open('./day14/input.txt', 'r') as f:
        template = f.readline().rstrip()
        
        f.readline()

        transforms = {x.split(' -> ')[0]: x.split(' -> ')[1].rstrip() for x in f.readlines()}

        return template, transforms

def add(counts, id):
    current = counts.get(id, 0)
    counts[id] = current + 1

template, transforms = load_input()

counts = {}
for pair in (template[i-1:i+1] for i in range(1, len(template))):
    add(counts, pair)

print(counts)

for i in range(40):
    new_res = {}
    for k,v in counts.items():
        if k in transforms:
            tfm = transforms[k]
            new_res[k[0] + tfm] = new_res.get(k[0] + tfm, 0) + v
            new_res[tfm + k[1]] = new_res.get(tfm + k[1], 0) + v
    
    counts = new_res

print(counts)

from collections import defaultdict

counter = defaultdict(int)
counter[template[-1]] += 1
counter[template[0]] += 1

for k,v in counts.items():
    counter[k[0]] += v / 2
    counter[k[1]] += v / 2

x = [int(i) for i in counter.values()]

print(max(x) - min(x))

        
    
