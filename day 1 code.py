print(max([sum([int(y) for y in x.split()]) for x in open('day 1 input.txt').read().split("\n\n")]))
print((sorted(([sum([int(y) for y in x.split()]) for x in open('day 1 input.txt').read().split("\n\n")]))[:-4:-1]))

#in one (dirty) line
a,b,c = sorted(([sum([int(y) for y in x.split()]) for x in open('day 1 input.txt').read().split("\n\n")]))[:-4:-1]; print(f"{a}, {a+b+c}")