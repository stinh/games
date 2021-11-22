import sys
a = sys.stdin.read()
b=a.split()
list=['星期五','星期六','星期日']
if b[0] in list:
    print("不開市")
else:
    print(int(b[1])*int(b[2]))