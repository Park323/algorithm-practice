def DFS(idx, contingency, visited):
    visited[idx] = True
    connected = list(iter_connection(idx, contingency[idx], visited))
    # print(visited)
    # print(connected)
    if connected:
        for ndx in connected:
            DFS(ndx, contingency, visited)
    else:
        return

def iter_connection(self_idx, array, visited):
    for idx, is_connected in enumerate(array):
        if is_connected and idx != self_idx and not visited.get(idx, False):
            yield idx

def complement(n, visited):
    return [i for i in range(n) if not visited.get(i)]
            
def solution(n, computers):
    n_networks = 0
    visited = {}
    while complement(n, visited):
        idx = complement(n, visited)[0]
        DFS(idx, computers, visited)
        n_networks += 1
    return n_networks