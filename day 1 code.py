print(max([sum([int(y) for y in x.split()]) for x in open('day 1 input.txt').read().split("\n\n")]))
print(sum(sorted(([sum([int(y) for y in x.split()]) for x in open('day 1 input.txt').read().split("\n\n")]))[-3:]))
