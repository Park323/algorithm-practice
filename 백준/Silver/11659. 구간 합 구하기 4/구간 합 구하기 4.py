import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
accums = [nums[0]]
for i, num in enumerate(nums[1:]):
    accums.append(accums[i] + num)

for _ in range(M):
    i, j = map(int, input().split())
    if i > 1:
        print(accums[j-1] - accums[i-2])
    else:
        print(accums[j-1])
