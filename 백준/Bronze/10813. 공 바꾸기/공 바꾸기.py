N, M = map(int, input().split())

bucket = [i+1 for i in range(N)]

for _ in range(M):
    i, j = map(int, input().split())
    tmp = bucket[i-1]
    bucket[i-1] = bucket[j-1]
    bucket[j-1] = tmp

print(" ".join(map(str, bucket)))