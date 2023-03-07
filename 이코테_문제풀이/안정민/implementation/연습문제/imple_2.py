# 문자열 재정렬
string = input()
answer = []
number = 0
for s in string:
    if ord(s) >= 65 and ord(s) <= 90:
        answer.append(s)
    else:
        number += int(s)

answer.sort()
answer.append(number)

for i in answer:
    print(i, end="")
