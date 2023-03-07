n = 1260 #거슬러줘야할 돈
count = 0

coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += n // coin #몫
    n %= coin #n-coin*몫
    
print(count)