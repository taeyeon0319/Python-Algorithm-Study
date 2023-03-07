import sys
N,M=map(int,sys.stdin.readline().split())
card=[]
for i in range(N):
    card.append(list(map(int,sys.stdin.readline().split())))
minn=[]
for i in card:
    minn.append(min(i))
    
print(max(minn))