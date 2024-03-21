from collections import deque

N, K = map(int, input().split())

queue = deque()

for n in range(1, N+1):
    queue.append(n)

series = []
    
count = 0
while queue:
    count += 1
    num = queue.popleft()
    if count == K:
        count = 0
        series.append(num)
    else:
        queue.append(num)

print("<"+", ".join(map(str, series))+">")