n=int(input())
coin=list(map(int, input().split()))
coin.sort()

target=1

for i in coin:
    if target<i:
        break
    
    target+=i

print(target)
