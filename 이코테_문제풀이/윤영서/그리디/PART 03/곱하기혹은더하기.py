import sys
#num=list(map(int,sys.stdin.readline().split()))
a=list(map(int,sys.stdin.readline().rstrip()))
print(a)
result=a[0]
for i in range(1,len(a)):
    if (a[i]<=1 and result==0):
        result+=a[i]
    else:
        result*=a[i]
print(result)
