def is_stopable(matrix, index):
    return index[0] >= 0 and index[1] >= 0 \
           and index[0] < len(matrix) and index[1] < len(matrix[0]) \
           and matrix[index[0]][index[1]] == 0

def turn_around(direction):
    order = [(1,0), (0,1), (-1,-1)]
    return order[(order.index(direction) + 1) % len(order)]

def get_next_index(index, direc):
    return [_i + _d for _i, _d in zip(index, direc)]

def solution(n):
    answer = [[0 for _ in range(n)] for _ in range(n)]
    
    index = [0,0]
    direc = (1,0)
    N = (n * (n + 1) // 2)
    for number in range(1, N+1):
        answer[index[0]][index[1]] = number
        n_index = get_next_index(index, direc)
        if is_stopable(answer, n_index):
            index = n_index
        else:
            direc = turn_around(direc)
            index = get_next_index(index, direc)

    ret = []
    for row in range(n):
        for num in answer[row][:row+1]:
            ret.append(num)
    
    return ret