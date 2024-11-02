from itertools import combinations

debug = False

if debug:
    import sys
    sys.stdin = open('input_1102.txt')
    input = sys.stdin.readline


def mask2bit(mask):
    bitmask = 0
    for k, v in enumerate(mask[::-1]):
        if v:
            bitmask += 2**k
    return bitmask

def bit2mask(bitmask, N):
    mask = [False for _ in range(N)]
    i = -1
    while bitmask != 0:
        if bitmask % 2:
            mask[i] = True
        else:
            mask[i] = False
        bitmask = bitmask // 2
        i -= 1
    return mask


def main():
    N = int(input())
    
    costs = [list(map(int, input().split())) for _ in range(N)]
    
    onoff = list(input().strip())
    
    P = int(input())
    
    dp = [float("inf") for _ in range(1<<N)]
    
    mask = [True if v == 'Y' else False for v in onoff]
    
    if sum(mask) >= P:
        print(0)
        return
    
    bitmask = mask2bit(mask)
    dp[bitmask] = 0
    
    for bitmask in range(1<<N):
        mask = bit2mask(bitmask, N)

        for i, ei in enumerate(mask):
            for j, ej in enumerate(mask):
                if i == j:
                    continue
                
                if ei and not ej:
                    new_mask = bitmask + 2**(N-j-1)
                    dp[new_mask] = min(dp[new_mask], dp[bitmask] + costs[i][j])
    
    answer = float("inf")
    for idxs in combinations(range(N), P):
        mask = [False for _ in range(N)]
        for idx in idxs:
            mask[idx] = True
        bitmask = mask2bit(mask)
        answer = min(answer, dp[bitmask])
    answer = -1 if answer == float('inf') else answer
    
    if debug:
        print("===============================")
        print(onoff)
        print('-------')
        for cost in costs:
            print(cost)
        print('-------')
        print(
            {bin(i)[2:]:cost for i, cost in enumerate(dp)}
        )
        print("===============================")
    print(answer)
    return answer


if debug:
    if __name__ == "__main__":
        T = int(input().strip())
        for t in range(T):
            print(f"[{t+1}th case]")
            main()
else:
    main()
