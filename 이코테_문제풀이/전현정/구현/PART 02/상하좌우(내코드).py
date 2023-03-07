import sys
N=int(sys.stdin.readline())
cmd=list(sys.stdin.readline().split())
pos=[1,1]
for i in cmd:
    if i=='R':
        if pos[1]<N:
            pos[1]+=1
    elif i=='U':
        if pos[0]>1:
            pos[0]-=1
    elif i=='L':
        if pos[1]>1:
            pos[1]-=1
    else:
        if pos[0]<N:
            pos[0]+=1
print(pos[0],pos[1])