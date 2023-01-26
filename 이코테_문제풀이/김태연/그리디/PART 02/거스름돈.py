n = int(input())
print("거슬러 받아야할 돈 : {}".format(n))

coin = 0

coin_types = [500,100,50,10]

for c in coin_types:
    coin += n//c
    n %= c

print("동전개수 : {}".format(coin))