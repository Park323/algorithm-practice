from copy import deepcopy

def is_valid_position(i, j, maps):
    return i >= 0 and i < len(maps) and j >= 0 and j < len(maps[0])

def available_directions(i, j, maps):
    available = []
    for i_offset, j_offset in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        i_n = i + i_offset
        j_n = j + j_offset
        if is_valid_position(i_n, j_n, maps) and maps[i_n][j_n]:
            available.append((i_n, j_n))
    return available

def DFS(i, j, maps):
    # Terminate condition
    if i == len(maps)-1 and j == len(maps[0])-1:
        return 1

    # Move (Only to opened directions)
    paths = []
    for i_n, j_n in available_directions(i, j, maps):
        new_maps = deepcopy(maps)
        new_maps[i_n][j_n] = 0
        if dist:=DFS(i_n, j_n, new_maps):
            paths.append(dist)
        # print((i_n, j_n), dist)
    if paths:
        return min(paths) + 1
    else:
        return None

def BFS(maps):
    """
    Map을 유지해주는 게 point.
    두 갈래 길이 한 점에서 중첩된다면 더 먼 쪽은 버려도 된다.
    """
    queue = [(0,0,0)] # (i, j, depth)
    while queue:
        i, j, depth = queue.pop(0)
        if i+1 == len(maps) and j+1 == len(maps[0]):
            return depth + 1
        for i_n, j_n in available_directions(i, j, maps):
            maps[i_n][j_n] = 0
            queue.append((i_n, j_n, depth+1))
    return -1

def solution(maps):
    # maps[0][0] = 0
    # answer = DFS(0, 0, maps)
    # answer = answer if answer is not None else -1
    
    answer = BFS(maps)
    
    return answer
