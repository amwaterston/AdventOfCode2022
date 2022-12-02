#part 1 in one line
print(sum([({0:3, -2: 6, 1: 6, -1: 0, 2: 0}[(ord(r[2]) - ord('X')) - (ord(r[0]) - ord('A'))] + (1 + ord(r[2]) - ord('X'))) for r in open('day 2 input.txt').read().strip().split("\n")]))

