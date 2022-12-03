
def solution(x, y):
    return int(((y+x-1) * (y+x) / 2) - (y - 1))

print(solution(5, 10))