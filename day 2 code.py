#part 1 in one line
print(sum([({0:3, -2: 6, 1: 6, -1: 0, 2: 0}[(x := ord(r[2]) - ord('X')) - (ord(r[0]) - ord('A'))] + (1 + x)) for r in open('day 2 input.txt').read().split("\n")]))
print(sum([((ord(r[0]) - ord('A') + ((w := ord(r[2]) - ord('X')) -1)) % 3) + 1 + (w * 3) for r in open('day 2 input.txt').read().split("\n")]))

