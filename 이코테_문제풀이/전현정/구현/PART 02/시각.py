#이코테 코드 - 완탐
h=int(input())

count=0
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i)+str(j)+str(k):#시,분,초
                count+=1
print(count)