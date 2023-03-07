#잃어버린 괄호
#식의 값을 가능한 한 작게 만드는 문제
#55-(50+40)
import sys
a=sys.stdin.readline()
b=a.split('-')#(b[0])-(b[1])-(b[2])

sum=0
for i in b[0].split('+'):
    sum+=int(i)
#b[0]의sum
for i in b[1:]:
    for j in i.split('+'):#b[i].split하면 안됨
        sum-=int(j)
#b[1]이후로의 sum들은 빼기
print(sum)