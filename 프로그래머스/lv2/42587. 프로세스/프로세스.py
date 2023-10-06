def solution(priorities, location):
    queue = priorities
    cnt = 0
    while queue:
        proc = queue.pop(0)
        if queue and proc < max(queue):
            if location == 0:
                location += len(queue) + 1
            queue.append(proc)
        else:
            cnt += 1
            if location == 0:
                return cnt
        location -= 1