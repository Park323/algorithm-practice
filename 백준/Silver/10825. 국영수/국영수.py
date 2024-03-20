N = int(input())

stu = []
for _ in range(N):
    items = input().split()
    name = items[0]
    kor, eng, mat = list(map(int,items[1:]))
    stu.append((-kor, eng, -mat, name))

stu = sorted(stu)
for _, _, _, name in stu:
    print(name)