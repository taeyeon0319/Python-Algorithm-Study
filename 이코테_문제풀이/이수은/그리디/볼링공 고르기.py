n, m=map(int, input().split())
ball=list(map(int, input().split()))
weight_list=[0]*(m+1)

for weight in ball:
    weight_list[weight]+=1

cnt=0
for i in range(1, m+1):
    n-=weight_list[i]
    cnt+=weight_list[i]*n

print(cnt)