dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
with open("day 8 input.txt") as fp:
    f = [list(l.strip()) for l in fp.readlines()]
    trees_spotted = 0
    max_ss = 0
    for y in range(len(f)):
        for x in range(len(f[0])):
            ss = 1
            tree_spotted = False
            for d in dirs:
                ssi = 0
                nx = x + d[0]
                ny = y + d[1]
                while (True):
                    ssi += 1
                    if nx < 0 or nx >= len(f[0]) or ny < 0 or ny >= len(f):
                        tree_spotted = True
                        ss = ss * (ssi - 1)
                        break
                    elif int(f[ny][nx]) >= int(f[y][x]):
                        ss = ss * ssi
                        break
                    nx = nx + d[0]
                    ny = ny + d[1]

            if tree_spotted:
                trees_spotted += 1
            max_ss = max(max_ss, ss)
                
    print(trees_spotted)
    print(max_ss)