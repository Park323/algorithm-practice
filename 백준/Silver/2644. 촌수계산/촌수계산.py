from collections import deque
import sys
input = sys.stdin.readline

def mii():
    return map(int, input().split())

def BFS():
    pass
           
def check_valid(i, j, I, J):
    return not (i < 0 or j < 0 or i >= I or j >= J)

N = int(input())
A, B = mii()
M = int(input())
graph = [[] for _ in range(N+1)]
dist = [-1 for _ in range(N+1)]
for _ in range(M):
    x, y = mii()
    graph[x].append(y)
    graph[y].append(x)

queue = deque()
queue.append(A)
dist[A] = 0
answer = -1
while queue:
    x = queue.popleft()
    for y in graph[x]:
        if dist[y] == -1:
            dist[y] = dist[x] + 1
            queue.append(y)
            if y == B:
                answer = dist[y]
                break

print(answer)