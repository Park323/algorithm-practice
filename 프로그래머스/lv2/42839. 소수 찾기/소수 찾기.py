from itertools import permutations, combinations

def is_prime(number):
    if number == 0 or number == 1:
        return False
    if number == 2:
        return True
    for d in range(2, number//2 + 1):
        if number % d == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    counted = {}
    for length in range(1, len(numbers)+1):
        for subset in combinations(numbers, length):
            for pair in permutations(subset):
                num = int(''.join(pair))
                if not counted.get(num) and is_prime(num):
                    answer += 1
                    counted[num] = True
    return answer