# 곱하기 혹은 더하기
n = input()
answer = 0
for i in n:
    if answer == 0:
        answer += int(i)
    elif i == "0" or i == "1":
        answer += int(i)
    else:
        answer *= int(i)
print(answer)
