#주유소//최소 비용으로 주유하여 일직선 도로를 달리는 문제
import sys
N=int(sys.stdin.readline())
length=list(map(int, sys.stdin.readline().split()))
cost=list(map(int,sys.stdin.readline().split()))

min_price=cost[0]*length[0]

min_cost=cost[0]

for i in range(1,N-1):
    if min_cost>cost[i]:
        min_cost=cost[i]
    min_price+=min_cost*length[i]
        #min_price+=min_cost*length[i]>>오답

print(min_price)