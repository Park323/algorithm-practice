from collections import deque
import sys
input = sys.stdin.readline

def mii():
    return map(int, input().split())

def BFS():
    pass
           
def check_valid(i, j, I, J):
    return not (i < 0 or j < 0 or i >= I or j >= J)

W, H = mii()
queue = deque()
cab = [[-1 for _ in range(W)] for _ in range(H)]
for h in range(H):
    for w, state in enumerate(mii()):
        cab[h][w] = state
        if state == 1:
            queue.append((h,w))

while queue:
    h, w = queue.popleft()
    dev = [(-1,0), (0,-1), (0, 1), (1, 0)]
    for dh, dw in dev:
        if check_valid(h+dh, w+dw, H, W) and cab[h+dh][w+dw] == 0:
            cab[h+dh][w+dw] = cab[h][w] + 1
            queue.append((h+dh, w+dw))

if min(min(abs(day) for day in days) for days in cab) == 0:
    print(-1)
else:
    min_day = max(max(days) for days in cab)
    print(min_day - 1)