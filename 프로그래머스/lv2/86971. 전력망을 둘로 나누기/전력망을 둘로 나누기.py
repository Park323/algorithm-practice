def cnt(root, graph, discon):
    total = 1
    for node in graph[root]:
        if node == discon:
            continue
        total += cnt(node, graph, root)
    return total

def solution(n, wires):
    graph = {key:[] for key in range(1, n+1)}
    
    for n1, n2 in wires:
        graph[n1].append(n2)
        graph[n2].append(n1)
    
    answer = 9999999999
    for n1, n2 in wires:
        if (disc := abs(cnt(n1, graph, n2) - cnt(n2, graph, n1))) < answer:
            answer = disc
    
    return answer