class Cave:

    def __init__(self, id):
        self.id = id
        self.routes = []
    
    def add_route(self, id):
        self.routes.append(id)
    
    def find_routes(self, caves, traversed):
        res = [traversed + [caves[i]] for i in self.routes if ((i.islower() and i not in [q.id for q in traversed]) or i.isupper())]
        return res

    def __repr__(self) -> str:
        return f'{self.id}'

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
        
        return data

caves = load_input()

kju = [[caves['start']]]
res = []
while len(kju) > 0:
    r = kju.pop(0)
    if r[-1].id == 'end':
        res.append(r)

    for i in r[-1].find_routes(caves, r):
        kju.append(i)

for i in res:
    print(' -> '.join((j.id for j in i)))

print(len(res))

