import math

data = input()

count=0

comp=int(data[0])
for i in range(1, len(data)):
    num=int(data[i])

    if comp!=num:
        count+=1
        comp=num

result=math.ceil(count/2)
print(result)
