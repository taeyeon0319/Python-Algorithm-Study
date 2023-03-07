n,k = map(int, input().split())

result=0

while n>=k:
    if(n%k!=0):
        n-=1
        result+=1
    else:
        n//=k
        result+=1

if(n>1):
    n-=1
    result+=1
print(result)
