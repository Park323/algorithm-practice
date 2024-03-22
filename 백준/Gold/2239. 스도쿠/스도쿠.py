import sys
input = sys.stdin.readline

def mii():
    return map(int, input().split())

def xy2groupidx(x,y):
    return (y//3) + (x//3)*3

board = [[0 for _ in range(9)] for _ in range(9)]
row_search = [[False for _ in range(10)] for _ in range(9)]
col_search = [[False for _ in range(10)] for _ in range(9)]
sub_search = [[False for _ in range(10)] for _ in range(9)]
for i in range(9):
    for j, num in enumerate(map(int, input().strip())):
        board[i][j] = num
        row_search[i][num] = True
        col_search[j][num] = True
        # import pdb;pdb.set_trace()
        # print(i, j, xy2groupidx(i,j))
        sub_search[xy2groupidx(i,j)][num] = True

def DFS(i,j):
    # print("<<",i,j,">>")
    # print(board)
    if i >= 9:
        return True
    if board[i][j] == 0:
        for num in range(1, 10):
            if row_search[i][num] or col_search[j][num] \
                or sub_search[xy2groupidx(i,j)][num]:
                    continue
            else:
                board[i][j] = num
                row_search[i][num] = True
                col_search[j][num] = True
                sub_search[xy2groupidx(i,j)][num] = True
                if DFS( i+(j+1)//9, (j+1)%9 ):
                    return True
                board[i][j] = 0
                row_search[i][num] = False
                col_search[j][num] = False
                sub_search[xy2groupidx(i,j)][num] = False
    elif DFS( i+(j+1)//9, (j+1)%9 ):
        return True
    return False

ret = DFS(0,0)
for row in board:
    print("".join(map(str, row)))
