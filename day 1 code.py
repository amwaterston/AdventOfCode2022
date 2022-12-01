print(max([sum([int(y) for y in x.split()]) for x in open('day 1 input.txt').read().split("\n\n")]))
print((sorted(([sum([int(y) for y in x.split()]) for x in open('day 1 input.txt').read().split("\n\n")]))[:-4:-1]))

print((s := sorted(([sum([int(y) for y in x.split()]) for x in open('day 1 input.txt').read().split("\n\n")]))[:-4:-1])[0],sum(s))