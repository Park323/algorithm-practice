from copy import deepcopy as copy

# 1) A 이어붙이기: AAA, AAAAAA
# 2) +
# 3) /
# 4) -
# 5) *

def add(x, y):
    return x + y

def divide(x, y):
    if y == 0:
        return -1
    return x // y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x*y

def get_nnn(x, n):
    y = 0
    for k in range(n):
        y += x * 10**k
    return y

# 5 55 555 5555
# 1 

def solution(N, number):
    count = 1
    counts = [-1 for _ in range(32001)]
    results = set()
    results.add(N)
    counts[N] = 1
    
    while count <= 8:
        rr = copy(results)
        for num1 in rr:
            cnt1 = counts[num1]
            for num2 in rr:
                cnt2 = counts[num2]
                for n in [
                            get_nnn(N, count),
                            add(num1, num2), 
                            subtract(num1,num2), 
                            divide(num1, num2), 
                            multiply(num1, num2)]:
                    if n <= 32000 and n >= 1:
                        if counts[n] == -1:
                            counts[n] = cnt1 + cnt2
                        else:
                            counts[n] = min(cnt1+cnt2, counts[n])
                        results.add(n)
        count += 1
    return counts[number]