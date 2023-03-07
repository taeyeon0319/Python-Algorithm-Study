# 왕실의 나이트

curr = input()

x = curr[0]
y = curr[1]

direc = [(1, 2), (-1, 2), (1, -2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]

x = ord(x) - 96

cnt = 0

for pos in direc:

    dx = x + pos[0]
    dy = int(y) + pos[1]

    if dx < 1 or dy < 1 or dx > 8 or dy > 8:
        continue

    cnt += 1

print(cnt)
