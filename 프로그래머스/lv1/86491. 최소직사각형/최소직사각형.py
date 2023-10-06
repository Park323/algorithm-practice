def solution(sizes):
    heights = []
    widths  = []
    for size in sizes:
        heights.append(min(size))
        widths.append(max(size))
    answer = max(heights) * max(widths)
    return answer