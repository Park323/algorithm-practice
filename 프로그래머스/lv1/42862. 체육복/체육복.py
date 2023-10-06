def solution(n, lost, reserve):
    new_lost = lost[:]
    new_reserve = reserve[:]
    for stu in lost:
        if stu in reserve:
            new_lost.remove(stu)
            new_reserve.remove(stu)
    lost, reserve = sorted(new_lost), new_reserve
    # print(lost, reserve)
    
    answer = n
    for stu in lost:
        if stu - 1 in reserve:
            reserve.remove(stu - 1)
        elif stu + 1 in reserve:
            reserve.remove(stu + 1)
        else:
            answer -= 1
    
    return answer