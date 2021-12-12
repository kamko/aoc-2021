from collections import Counter, deque

class Cave:

    def __init__(self, id):
        self.id = id
        self.routes = []
    
    def add_route(self, id):
        if self.id == 'end':
            return
        if id == 'start':
            return

        self.routes.append(id)
    
    def find_routes(self, caves, traversed):
        res = []
        
        freq = Counter((i.id for i in traversed if (i.id.islower() and i.id != 'start')))
        for r in self.routes:
            if r.isupper():
                res.append(traversed + [caves[r]])
            
            if r.islower():
                if len(freq) == 0:
                    res.append(traversed + [caves[r]])
                elif r in freq and freq.most_common(1)[0][1] == 1:
                    res.append(traversed + [caves[r]])
                elif r not in freq:
                    res.append(traversed + [caves[r]])

        return res

    def __repr__(self) -> str:
        return f'[{self.id}]'

def load_input():
    with open('./day12/input.txt', 'r') as f:
        data = {}

        for i in f.readlines():
            i = i.rstrip()

            fr = i.split('-')[0]
            to = i.split('-')[1]

            fr_cave = data.get(fr, Cave(fr))
            fr_cave.add_route(to)
            data[fr] = fr_cave

            to_cave = data.get(to, Cave(to))
            to_cave.add_route(fr)
            data[to] = to_cave

        print(data)
        return data

caves = load_input()

kju = deque()
kju.append([caves['start']])
res = []
while len(kju) > 0:
    r = kju.popleft()
    if r[-1].id == 'end':
        res.append(r)

    for i in r[-1].find_routes(caves, r):
        kju.append(i)

for i in res:
    print(' -> '.join((j.id for j in i)))

print(len(res))

