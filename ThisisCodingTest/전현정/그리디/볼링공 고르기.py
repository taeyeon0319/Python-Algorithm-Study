import sys
N,M=map(int,sys.stdin.readline().split())
ball=list(map(int,sys.stdin.readline().split()))
cnt=0
for i in range(N):
    cnt+=i

for i in range(1,M+1):
    temp=ball.count(i)
    if temp>=2:
        cnt2=0
        for i in range(temp):
            cnt2+=i
        cnt-=cnt2

print(cnt)