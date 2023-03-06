# 만들 수 없는 금액

n = int(input())

coins = list(map(int, input().split()))
coins.sort()
print(coins)
target = 1

for c in coins:
    if target < c:
        break
    else:
        target += c

print(target)
