def solution(clothes):
    closet = {}
    for value, key in clothes:
        closet[key] = closet.get(key, 0) + 1
    
    answer = 1
    for value in closet.values():
        answer *= value + 1
    answer -= 1
    
    return answer