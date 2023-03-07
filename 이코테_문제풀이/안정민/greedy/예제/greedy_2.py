# 숫자 카드 게임

n, m = map(int, input().split())
arr = [] * n
answer = 0
for i in range(n):
    arr.append(list(map(int, input().split())))
    answer = max(min(arr[i]), answer)
print(answer)
