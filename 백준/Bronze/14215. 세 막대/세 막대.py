lines = list(map(int,input().split()))

lines = sorted(lines)

if lines[2] < lines[0] + lines[1]:
    print(sum(lines))
else:
    l = lines[0] + lines[1]
    print(l + l - 1)