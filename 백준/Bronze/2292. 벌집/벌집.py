N =int(input())

def max_range(dist):
    return 3 * (dist ** 2 + dist) + 1

for dist in range(100000):
    if max_range(dist) >= N:
        print(dist+1)
        break