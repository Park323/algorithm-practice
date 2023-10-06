def solution(s):
    stack = []
    for ch in s:
        if ch not in ["(", ")"]:
            continue
        if stack and ch == ")" and stack[-1] == "(":
            stack.pop()
        else:
            stack.append(ch)
    
    if stack:
        return False
    else:
        return True