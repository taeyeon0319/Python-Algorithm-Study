import sys
n,m,k=map(int,sys.stdin.readline().split())
array=list(map(int,sys.stdin.readline().split()))
array.sort(reverse=True)
#print(array)

result=0
#가장 큰 수를 K번 더하고 두번째로 큰수를 한번,가장 큰수 K번..//while문
#count없이 M횟수 1씩 차감,m==0일 때 break
while True:
    for i in range(k):
        if m==0:
            break
        result+=array[0]
        m-=1
    if m==0:
        break
    result+=array[1]
    m-=1

print(result)


    
