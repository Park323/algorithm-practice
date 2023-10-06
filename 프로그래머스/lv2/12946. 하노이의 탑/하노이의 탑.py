def recursive(start, middle, end, n):
    if n == 1:
        return [[start, end]]
    return [*recursive(start, end, middle, n-1), [start, end], *recursive(middle, start, end, n-1)]

def solution(n):
    answer = recursive(1, 2, 3, n)    
    return answer