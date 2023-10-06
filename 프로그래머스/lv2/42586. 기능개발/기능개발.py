from math import ceil

def solution(progresses, speeds):
    answer = []
    last_dist = 0
    queue = list(zip(progresses, speeds))
    while queue:
        process, speed = queue.pop(0)
        dist = ceil((100 - process) / speed)
        if dist > last_dist:
            last_dist = dist
            answer.append(1)
        else:
            answer[-1] += 1
    return answer