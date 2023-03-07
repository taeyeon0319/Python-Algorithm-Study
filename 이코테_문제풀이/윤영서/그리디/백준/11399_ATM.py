#ATM 사람 N명, 걸리는 시간 Pi 
#P1=3,P2=1,P3=4,P4=3,P5=2이면 필요한 시간의 합(이 순서대로면 3+4+8+11+13)의 최솟값
#기다리는 시간의 합을 최소화하는 문제
import sys
N=int(sys.stdin.readline())
p=list(map(int,sys.stdin.readline().split()))
p.sort()
result=0
for i in range(1,N+1):#1부터 N까지
    result+=sum(p[:i])# 1부터 N-1까지
#p[i:] >>i이상 ,p[:i] >>i미만, p[a:b] >>a이상 b미만
#for i in range(1,N):
#answer+=sum(p[:i])
#print(answer)
print(result)



