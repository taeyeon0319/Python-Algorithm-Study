n, m = map(int, input().split())
w = list(map(int, input().split()))

cnt = 0

for i in range(len(w)):
    for j in range(i, len(w)):
        if w[i]!=w[j]:
            cnt+=1

print(cnt)

