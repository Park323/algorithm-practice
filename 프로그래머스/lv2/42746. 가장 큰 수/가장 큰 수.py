"""
Bubble sort style (실패: O(n^2))
"""
def sum_str(numbers):
    ret = ""
    for num in numbers:
        ret += str(num)
    return int(ret)

def solution_bubble(numbers):
    for j in range(1, len(numbers)):
        for i in range(len(numbers) - j):
            if sum_str([numbers[i], numbers[i+1]]) < sum_str([numbers[i+1], numbers[i]]):
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
    
    return str(sum_str(numbers))

"""
맘에 안듦
"""
import re
def solution(numbers):
    numbers = [str(num) * 3 for num in numbers]
    numbers.sort(reverse=True)
    numbers = [num[:len(num)//3] for num in numbers]
    answer =  "".join(numbers)
    return re.sub("^0+", "0", answer)