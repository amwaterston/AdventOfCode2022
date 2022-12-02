def solution(x, y):
    dx = (x * (x + 1))/2
    dy = ((y * (y + 1))/2)
    print((dx, dy))
    return int(dx) + int(dy)

print(solution(1, 4))