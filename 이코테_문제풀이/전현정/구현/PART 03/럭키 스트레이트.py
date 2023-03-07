import sys
score=sys.stdin.readline().strip()
a=0
b=0
for i in range(int(len(score)/2)):
    a+=int(score[i])
    b+=int(score[i+int(len(score)/2)])
if a==b:
    print('LUCKY')
else:
    print('READY')