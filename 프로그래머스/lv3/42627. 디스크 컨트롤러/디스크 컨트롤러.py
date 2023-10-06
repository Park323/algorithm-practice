from heapq import *
import math

def execute(time, heap, pending, terminate=999999999):
    while heap and time < terminate:
        length, start, idx = heappop(heap)
        time = max(time, start) + length
        pending[idx] = time - start
    return time

def solution(jobs):
    jobs  = sorted(jobs)        # Sorted by the requested order
    time  = 0                   # Last process ends
    queue = []                  # Heap
    pending = [0 for _ in jobs] # Waited time cots
    
    idx = 0
    while idx < len(jobs):
        start, length = jobs[idx]
        
        # print(idx, start, length, time, queue)
        time = execute(time, queue, pending, start) # Execute processes in Queue
        # print(idx, start, length, time, queue)
        heappush(queue, (length, start, idx)) # Save process to Queue
        # print(idx, start, length, time, queue)
        
        idx += 1
        
    if queue:
        time = execute(time, queue, pending) # Run processes & Clear Queue
    
    return math.floor(sum(pending)/len(pending)) # Floor !!