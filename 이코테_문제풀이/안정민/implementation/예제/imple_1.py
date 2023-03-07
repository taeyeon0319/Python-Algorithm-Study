# 상하좌우

n = int(input())

arr = list(input().split())

direct = ["L", "R", "U", "D"]
pos = [(0, -1), (0, 1), (-1, 0), (1, 0)]
x, y = 1, 1

for i in range(len(arr)):
    dx = x + pos[direct.index(arr[i])][0]
    dy = y + pos[direct.index(arr[i])][1]

    if dx > n or dy > n or dx < 1 or dy < 1:
        continue
    x = dx
    y = dy


print(x, y)
