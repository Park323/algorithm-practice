import sys
input = sys.stdin.readline

def mii():
    return map(int, input().split())

N, M = mii()
array = list(mii())

left = max(array)
right = sum(array)

ans = right
while left <= right:
    
    cnt = 1
    total = 0

    mid = (left + right) // 2

    # print(left, mid, right)

    for i, num in enumerate(array):
        # print("total", total)
        if total + num > mid:
            cnt += 1
            total = num
        else:
            total += num

    # print("cnt", cnt)

    if cnt <= M:
        right = mid-1
    else:
        left = mid+1

print(left)
