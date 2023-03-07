#
import sys
N=int(sys.stdin.readline())
array=list(map(int,sys.stdin.readline().split()))
array.sort()
#1 1 2 3 9
cost=0
for i in array:
    if cost+1<i:
        break
    else:
        cost+=i
#cost>0>1>2>5>8
print(cost+1)