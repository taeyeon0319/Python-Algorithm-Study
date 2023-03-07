num = list(map(int, input()))
result = num[0]

for i in range(1, len(num)):
    x = int(num[i])
    if(x<=1 or result<=1):
        result += num[i]
    else:
        result *= num[i]
    


print(result)
