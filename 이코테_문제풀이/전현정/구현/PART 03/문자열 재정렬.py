#내코드
'''
#문제의 설명에서 문자열에 숫자가 포함되지 않은 형태로 구성된 경우에 대한 설명을 추가하였으면 함. 0을 뒤에 붙이는지 아닌지.
import sys
S=sys.stdin.readline().strip()
number=0
abc=[]
for i in S:
    temp=ord(i)
    if temp<60:
        number+=int(i)
    else:
        abc.append(i)
abc.sort()
for i in abc:
    print(i,end='')
print(str(number))
'''
#모범답안
data = input()
result=[]
value = 0

for x in data:
    if x.isalpha():
        result.append(x)
    else:
        value += int(x)
        
result.sort()

if value !=0:
    result.append(str(value))
    
print(''.join(result))