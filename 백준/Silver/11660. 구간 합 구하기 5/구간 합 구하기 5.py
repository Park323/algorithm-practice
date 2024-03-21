import sys
input = sys.stdin.readline

N, M = map(int, input().split())

accums = [[0 for _ in range(N+1)] for _ in range(N+1)]
for r in range(1, N+1):
    row = [None, *list(map(int, input().split()))]
    for c in range(1, N+1):
        accums[r][c] = row[c] + accums[r-1][c] + accums[r][c-1] - accums[r-1][c-1]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    print(accums[x2][y2] - accums[x1-1][y2] - accums[x2][y1-1] + accums[x1-1][y1-1])
