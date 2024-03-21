from itertools import combinations

def manhatten_dist(x1,y1,x2,y2):
    return abs(x1-x2) + abs(y1-y2)


N, K = map(int,input().split())

coords = []

for _ in range(N):
    x, y = map(int,input().split())
    coords.append((x,y))

ret = []
for indices in combinations(range(N), K):
    mins = []
    for x2, y2 in coords:
        dists = []
        for idx in indices:
            x1, y1 = coords[idx]
            dist = manhatten_dist(x1,y1,x2,y2)
            dists.append(dist)
        mins.append(min(dists))
    ret.append(max(mins))

print(min(ret))
