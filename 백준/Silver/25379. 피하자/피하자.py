N = int(input())
array = []
for n in map(int, input().split()):
    array.append(n%2)

results = []
for flag in [0,1]:
    cnt = 0
    left = 0
    for i, n in enumerate(array):
        if n != flag:
            cnt += i - left
            left += 1
        else:
            pass
    results.append(cnt)
print(min(results))
