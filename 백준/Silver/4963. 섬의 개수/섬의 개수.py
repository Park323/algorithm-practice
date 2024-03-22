import sys
input = sys.stdin.readline

def mii():
    return map(int, input().split())

def DFS(h, w, mp):
    paths = [(-1,-1), (-1,0), (-1,1),
             (0,-1),  (0, 1),
             (1,-1),  (1, 0), (1, 1)]
    cnt = 0
    for dh, dw in paths:
        if (nh:=h+dh)>=0 and nh<len(mp) \
            and (nw:=w+dw)>=0 and nw<len(mp[0]) \
                and mp[nh][nw]:
            cnt += DFS(nh, nw, mp)
    
    return cnt
           
def check_valid(i, j, I, J):
    return not (i < 0 or j < 0 or i >= I or j >= J)

while True:
    W, H = mii()
    
    if W==0 and H==0:
        break
    
    mp = [None for _ in range(H)]
    for h in range(H):
        mp[h] = list(mii())
    
    cnt = 0
    while sum(sum(array) for array in mp):
        stack = []
        # Check unvisited
        for h in range(H):
            for w in range(W):
                if mp[h][w]:
                    mp[h][w] = 0
                    stack.append((h, w))
                    break
            if stack: 
                cnt += 1
                break

        while stack:
            # print(stack)
            h, w = stack.pop()
            # print("pop", (h,w))
            
            dev = [(-1,-1), (-1,0), (-1,1),
                (0,-1),          (0, 1),
                (1,-1),  (1, 0), (1, 1)]
            
            for dh, dw in dev:
                if check_valid(h+dh, w+dw, H, W) and mp[h+dh][w+dw]:
                    mp[h+dh][w+dw] = 0
                    stack.append((h+dh, w+dw))

    print(cnt)