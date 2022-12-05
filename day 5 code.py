crates, moves = open("day 5 input.txt").read().split("\n\n")
crates = [[row[i+1] for i in range(0, len(row), 4)] for row in list(reversed(crates.split("\n")[:-1]))]
stacks = [ [] for _ in range(len(crates[0])) ]

for r in crates:
    for c in range(len(r)):
        if (r[c]) != " ":
            stacks[c].append(r[c])

for m in moves.split("\n"):
    _, n, _, a, _, b = m.split(" ")
    t = []
    [t.append(stacks[int(a) - 1].pop()) for _ in range(int(n))]
    stacks[int(b) - 1].extend(list(reversed(t)))

print("".join([s[-1] for s in stacks]))