import sys
n=int(sys.stdin.readline())
a=[]
a=list(map(int,sys.stdin.readline().split()))
a.sort()
count=0
result=0
for i in range(len(a)):
    count+=1
    h=a[i]
    if count==h:
        result+=1
        count=0

print(result)
