num = list(map(int, input()))
cnt1 = 0
cnt2 = 0
#모두 1로 바꿀 때
for i in range(0, len(num)):
    if(num[i-1]!=num[i]):
        if(num[i]==0):
            cnt1+=1

#모두 0으로 바꿀 때
for i in range(0, len(num)):
    if(num[i-1]!=num[i]):
        if(num[i]==0):
            cnt2+=1

print(min(cnt1, cnt2))
