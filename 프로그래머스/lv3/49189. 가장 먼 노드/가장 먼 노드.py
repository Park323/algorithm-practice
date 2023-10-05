from copy import deepcopy
from itertools import groupby

def solution(n, edge):
    graph = {i:[] for i in range(1, n+1)}
    visited = {i:False for i in range(1, n+1)}
    dists = {i:-1 for i in range(1, n+1)}
    dists[1] = 0
    
    for e in edge:
        graph[e[0]] += [e[1]]
        graph[e[1]] += [e[0]]
    
    # print(graph)
    
    queue = [1]
    visited[1] = True
    last_dist = -1
    while queue:
        head = queue.pop(0)
        while graph[head]:
            leave = graph[head].pop(0)
            if not visited[leave]:
                queue.append(leave)
                visited[leave] = True
                dists[leave] = dists[head] + 1
                last_dist = dists[leave]

    answer = 0
    for key, dist in dists.items():
        if dist == last_dist:
            answer += 1

    return answer