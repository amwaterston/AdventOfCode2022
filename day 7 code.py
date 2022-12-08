class Dir:
    def __init__(self, name):
        self.name = name
        self.dirs = []
        self.files = []
        self.parent = None

    def cd(self, dir):
        d = Dir(dir)
        d.parent = self
        self.dirs.append(d)
        return d

    def size(self):
        return sum([dir.size() for dir in self.dirs]) + sum([file[1] for file in self.files])

    def total_size_less_100k(self):
        t = 0
        if (self.size() <= 100000):
            t += self.size()
        if (len(self.dirs) == 0):
            return t
        return t + sum([dir.total_size_less_100k() for dir in self.dirs])

    def smallest_delete(self, size):
        if (self.size() < size):
            return None
        s = list(filter(None, [dir.smallest_delete(size) for dir in self.dirs]))
        if len(s) > 0:
            return min(s)
        else: 
            return self.size()

with open("day 7 input.txt") as fp:
    ls = [l.strip() for l in fp.readlines()]
    cwd = []
    root = Dir("/")
    c = 0
    while c < len(ls):
        l = ls[c]
        #print(l)
        c = c + 1
        if (l[0] == "$"):
            _, cmd, *args = l.split()
            if cmd == "cd":
                if args[0] == "/":
                    cwd = root
                elif args[0] == "..":
                    cwd = cwd.parent
                else:
                    cwd = cwd.cd(args[0])
            elif cmd == "ls":
                while c < len(ls) and (l := ls[c])[0] != "$":
                    a, b = l.split()
                    if a != "dir":
                        cwd.files.append((b, int(a)))
                    c = c + 1

print(root.total_size_less_100k())

fs = 70000000 - root.size()
sn = 30000000 - fs

print(root.smallest_delete(sn))