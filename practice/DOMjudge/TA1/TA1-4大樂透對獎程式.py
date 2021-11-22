import sys
a = sys.stdin.read()
b=a.split(',')
buy=b[0].split()
com=b[1].split()
x=0
if buy[0] in com:
    x=x+1
if buy[1] in com:
    x=x+1 
if buy[2] in com:
    x=x+1 
if buy[3] in com:
    x=x+1 
if buy[4] in com:
    x=x+1 
if x <3:
    print(0)
elif x==3:
    print(100)
elif x==4:
    print(1000)
else:
    print(10000)