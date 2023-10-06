from itertools import groupby

def solution(arr):
    answer = [x[0] for x in groupby(arr)]
    return answer