import sys
import math
a=sys.stdin.read()
if '+' in a:
    b=a.split('+')
    print(int(b[0])+int(b[1]))
elif '-' in a:
    b=a.split('-')
    print(int(b[0])-int(b[1]))
elif '*' in a:
    b=a.split('*')
    print(int(b[0])*int(b[1]))
else:
    b=a.split('/')    
    print(math.floor(int(b[0])/int(b[1])))