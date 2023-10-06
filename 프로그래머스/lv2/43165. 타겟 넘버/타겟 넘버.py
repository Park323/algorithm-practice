def n_methods(root, numbers, target):
    nm = 0
    
    if len(numbers) == 0:
        # print(root, numbers, target)
        if root == target:
            nm += 1
    else:
        for sign in [-1, 1]:
            subroot = root + sign * numbers[0]
            nm += n_methods(subroot, numbers[1:], target)
    # print(root, target, nm, numbers)
    return nm
    

def solution(numbers, target):
    return n_methods(0, numbers, target)