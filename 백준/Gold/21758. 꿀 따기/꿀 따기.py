N = int(input())

array = list(map(int, input().split()))
accums = [0 for _ in range(N)]
for n in range(N):
    if n:
        accums[n] = accums[n-1] + array[n]
    else:
        accums[n] = array[n]

# Honey is on left
# H ... B1
maximum = 0
for i in range(1,N-1):
    reward = (accums[-1] - array[-1] - array[i]) + (accums[i] - array[i])
    maximum = max(reward, maximum)

# Honey on right
# B1 ... H
for i in range(1,N-1):
    reward = (accums[-1] - array[0] - array[i]) + (accums[-1] - accums[i])
    maximum = max(reward, maximum)

# Honey on middle
# B1 ... B2
for i in range(1,N-1):
    reward = accums[-1] + array[i] - array[0] - array[-1]
    maximum = max(reward, maximum)
print(maximum)
