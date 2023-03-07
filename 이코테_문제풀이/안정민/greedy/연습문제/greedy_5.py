# 볼링공 고르기

from itertools import combinations

n, m = map(int, input().split())
kg = list(map(int, input().split()))
cnt = 0
for i in combinations(kg, 2):
    if i[0] == i[1]:
        continue
    cnt += 1
print(cnt)
