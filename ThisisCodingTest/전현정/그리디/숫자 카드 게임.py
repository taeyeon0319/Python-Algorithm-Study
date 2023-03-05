import sys
n,m=map(int,sys.stdin.readline().split())

result=0
for i in range(n):
    data = list(map(int,sys.stdin.readline().split()))
    min_value = min(data)
    result = max(result,min_value)
print(result)