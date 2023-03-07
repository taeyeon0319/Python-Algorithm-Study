# 1이 될 때까지

"""
나누어 떨어지면 무조건 나누는게 최소 횟수
"""

n, k = map(int, input().split())
cnt = 0
while n != 1:
    if n % 5 == 0:
        n /= 5
    else:
        n -= 1
    cnt += 1
print(cnt)
