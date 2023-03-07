n = int(input())
x = list(map(int, input().split()))
result = 0

x.sort()
for i in range(len(x)-1):
    result += x[i]/2

result+=x[-1]
print(result)