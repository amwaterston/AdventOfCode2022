l = open("day 6 input.txt").read().strip()
print([len(set(l[i:i+4])) == 4 for i in range(len(l))].index(True) + 4)
print([len(set(l[i:i+14])) == 14 for i in range(len(l))].index(True) + 14)
