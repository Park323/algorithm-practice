def solution(brown, yellow):

    prod = brown + yellow
    sum_ = brown / 2 + 2
    
    for h in range(3, prod // 2 + 1):
        if prod % h != 0:
            continue
        w = prod // h
        if h + w == sum_:
            return [w, h]