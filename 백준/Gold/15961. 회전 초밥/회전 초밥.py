import sys
input = sys.stdin.readline

def mii():
    return map(int, input().split())

N, d, k, c = mii()

table = []
for _ in range(N):
    table.append(int(input()))

stype = [0 for _ in range(d+1)]
stype[c] = 1

slidesum = [0 for _ in range(N)]
slidesum[0] = 1

for i in range(k):
    if stype[table[i]] == 0:
        slidesum[0] += 1
    stype[table[i]] += 1

maximum = slidesum[0]
for i in range(N-1):
    prev_sushi = table[i]
    stype[prev_sushi] -= 1
    prev_num = 0 if stype[prev_sushi] else -1
    
    next_sushi = table[(i+k)%N]
    next_num = 0 if stype[next_sushi] else 1
    stype[next_sushi] += 1
    
    slidesum[i+1] = slidesum[i] + prev_num + next_num
    maximum = max(maximum, slidesum[i+1])
    
print(maximum)
