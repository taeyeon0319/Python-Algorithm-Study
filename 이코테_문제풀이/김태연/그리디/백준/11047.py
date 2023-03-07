n, k = map(int, input().split())
money_list = []
cnt = 0

for i in range(n):
    money = int(input())
    money_list.append(money)

for i in range(1, n+1):
    if k>=money_list[-i]:
        cnt+=k//money_list[-i]
        k%=money_list[-i]

print(cnt)