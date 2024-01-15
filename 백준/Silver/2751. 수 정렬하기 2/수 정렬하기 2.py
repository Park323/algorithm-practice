import sys

N=int(input())

for num in sorted([int(sys.stdin.readline()) for _ in range(N)]):
    print(num)