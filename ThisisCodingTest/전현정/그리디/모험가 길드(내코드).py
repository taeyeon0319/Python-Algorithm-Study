import sys

sys.stdin.readline()
m=list(map(int,sys.stdin.readline().split()))
m.sort()

res=0
mlist=[]
for i in m:
    if i==1:
        res+=1
    else:
        mlist.append(i)
        if len(mlist)==mlist[-1]:
            mlist=[]
            res+=1

print(res)