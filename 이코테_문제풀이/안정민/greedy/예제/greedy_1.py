# 큰수의 법칙
n, m, k = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
arr = arr[::-1]

answer = 0
cnt = 0
for i in range(m):
    if cnt == k:
        answer += arr[1]
        cnt = 0
    else:
        answer += arr[0]
    cnt += 1
print(answer)
