import sys
sys.stdin.readline()
coin=list(map(int,sys.stdin.readline().split()))
coin.sort(reverse=True)
for i in range(1,sum(coin)):
    temp=i
    flag=False
    for j in coin:
        if j<=temp:
            temp-=j
        if temp==0:
            flag=True
            break
        
    if flag==False:
        print(i)
        break
    
        