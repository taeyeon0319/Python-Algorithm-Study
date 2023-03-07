# 시각

n = int(input())
cnt = 0

for h in range(n + 1):
    for m in range(60):
        for s in range(60):
            if "3" in str(h) + str(m) + str(s):
                cnt += 1
print(cnt)


"""
왜 따로따로 하면 안되지??
str(h) 에 있는 3
str(m) , str(s)
"""
