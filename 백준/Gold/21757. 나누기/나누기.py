import sys
input = sys.stdin.readline

N = int(input())

series = list(map(int, input().split()))

accums = [0]
for i, num in enumerate(series, start=1):
    accums.append(accums[i-1] + num)

def search(idx, anchor, total, accums):
    cnt = 0
    for i in range(anchor, len(accums)):
        # print(accums[i], total/idx, total, idx)
        if accums[i] == total / 4 * idx:
            if idx == 4:
                cnt += 1
            else:
                cnt += search(idx+1, i+1, total, accums)
    return cnt

total = accums[-1]

if total % 4 != 0 :
    print(0)
else:
    cnt = search(1, 1, total, accums)

    print(cnt)

