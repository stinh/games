import sys
a = sys.stdin.read()

b = a.split()[0]

c = a.split()[1:]

print(c[int(b) - 1])