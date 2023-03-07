import sys
N,M=map(int,sys.stdin.readline().split())
#print(N)
#print(M)
array=list(map(int,sys.stdin.readline().split()))
#print(array[4])
result=0
for i in range(N-1):
    for j in range(i+1,N):
        if array[i]!=array[j]:
            result+=1

print(result)