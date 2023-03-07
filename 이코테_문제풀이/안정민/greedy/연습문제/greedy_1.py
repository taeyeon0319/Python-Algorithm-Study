# 모험가 길드
n = int(input())

arr = list(map(int, input().split()))

arr.sort()
answer = 0
cnt = 0

for i in arr:

    cnt += 1
    if cnt >= i:
        answer += 1
        cnt = 0
print(answer)
