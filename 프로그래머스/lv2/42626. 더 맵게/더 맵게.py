import heapq

def mix(sc1, sc2):
    return sc1 + sc2 * 2

def swap(heap, i1, i2):
    heap[i1], heap[i2] = heap[i2], heap[i1]
    return i2

def pop(heap):
    minimum, heap[1] = heap[1], heap[-1]
    heap[:] = heap[:-1]
    
    i = 1
    while 2*i < len(heap):
        if 2*i + 1 >= len(heap) or heap[2*i] <= heap[2*i+1]:
            j = 2*i
        else:
            j = 2*i + 1
        if heap[i] > heap[j]:
            i = swap(heap, i, j)
        else:
            break
    return minimum

def push(heap, node):
    heap.append(node)
    i = len(heap) - 1
    while i//2 > 0:
        if heap[i] < heap[i//2]:
            i = swap(heap, i, i//2)
        else:
            break

def solution(scoville, K):
    ## Heapq
    scoville.sort()
    total_mix = 0
    
    while len(scoville) > 1:
        if scoville[0] >= K:
            return total_mix
        sc1 = heapq.heappop(scoville)
        sc2 = heapq.heappop(scoville)
        msc = mix(sc1, sc2)
        total_mix += 1
        heapq.heappush(scoville, msc)
    if scoville[0] >= K:
        return total_mix
    return -1

    ## My own
    
#     # Sort
#     _sc = [None]
#     for sc in scoville:
#         push(_sc, sc)
#     scoville = _sc
    
#     Pop & Mix
#     total_mix = 0
#     if scoville[1] >= K: # 시작부터 K 이상인 경우!!!
#         return total_mix
#     while len(scoville) > 2:
#         sc1 = pop(scoville)
#         sc2 = pop(scoville)
#         mix_sc = mix(sc1, sc2)
#         total_mix += 1
#         push(scoville, mix_sc)
#         if scoville[1] >= K:
#             return total_mix
#     return -1

    ## Python sort
    # scoville = sorted(scoville)
    # total_mix = 0
    # while len(scoville) > 1:
    #     sc1 = scoville.pop(0)
    #     sc2 = scoville.pop(0)
    #     mix_sc = mix(sc1, sc2)
    #     total_mix += 1
    #     scoville.append(mix_sc)
    #     scoville = sorted(scoville)
    #     if scoville[0] >= K:
    #         return total_mix
    # return -1