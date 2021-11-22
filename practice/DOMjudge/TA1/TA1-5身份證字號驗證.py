import sys
a=sys.stdin.read()
c=0
if a[0] == 'A':
    c = 1 + 0 * 9
if a[0] == 'a':
    c = 1 + 1 * 9
if a[0] == 'C':
    c = 1 + 2 * 9
if a[0] == 'D':
    c = 1 + 3 * 9
if a[0] == 'E':
    c = 1 + 4 * 9
if a[0] == 'F':
    c = 1 + 5 * 9
if a[0] == 'G':
    c = 1 + 6 * 9
if a[0] == 'H':
    c = 1 + 7 * 9
if a[0] == 'I':
    c = 3 + 4 * 9
if a[0] == 'J':
    c = 1 + 8 * 9
if a[0] == 'K':
    c = 1 + 9 * 9
if a[0] == 'L':
    c = 2 + 0 * 9
if a[0] == 'M':
    c = 2 + 1 * 9
if a[0] == 'N':
    c = 2 + 2 * 9
if a[0] == 'O':
    c = 3 + 5 * 9
if a[0] == 'P':
    c = 2 + 3 * 9
if a[0] == 'Q':
    c = 2 + 4 * 9
if a[0] == 'R':
    c = 2 + 5 * 9
if a[0] == 'S':
    c = 2 + 6 * 9
if a[0] == 'T':
    c = 2 + 7 * 9
if a[0] == 'U':
    c = 2 + 8 * 9
if a[0] == 'V':
    c = 2 + 9 * 9
if a[0] == 'W':
    c = 3 + 2 * 9
if a[0] == 'X':
    c = 3 + 0 * 9
if a[0] == 'Y':
    c = 3 + 1 * 9
if a[0] == 'Z':
    c = 3 + 3 * 9
d = int(a[1])
e = int(a[2])
f = int(a[3])
g = int(a[4])
h = int(a[5])
i = int(a[6])
j = int(a[7])
k = int(a[8]) 
l = int(a[9]) 
if (c+d*8+e*7+f*6+g*5+h*4+i*3+j*2+k+l)%10 == 0:
    print('合法')
else:
    print('不合法')