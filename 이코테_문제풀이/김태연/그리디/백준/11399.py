n = int(input())
t = list(map(int, input().split()))
t.sort()
sum=0

for i in range(n):
    for j in range(i+1):
        sum+=t[j]
        
print(sum)