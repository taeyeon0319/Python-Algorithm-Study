# 럭키 스트레이트

n = input()
length = int(len(n) / 2)

n1 = n[:length]
n2 = n[length:]
sum1, sum2 = 0, 0

for i, j in zip(n1, n2):
    sum1 += int(i)
    sum2 += int(j)

if sum1 == sum2:
    print("LUCKY")
else:
    print("READY")
