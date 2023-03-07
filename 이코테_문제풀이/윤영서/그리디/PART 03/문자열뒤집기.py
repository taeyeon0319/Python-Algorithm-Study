import sys
a=list(map(int,sys.stdin.readline().rstrip()))
a.reverse()
print(a)
first=a[0]
count_0=0 #0그룹 수//first가 0이면 1+(1>0)바뀌는 횟수
count_1=0 #1그룹 수
#1-0=1//0-1=-1//1-1=0//0-0=0
if first==0:
    count_0=1
else:
    count_1=1
#print(count_0)
#print(count_1)
for i in range(len(a)-1):
    h=a[i+1]-a[i]
    if h==1:
        count_1+=1
    elif h==-1:
        count_0+=1
    else:
        pass

#print(count_0)
#print(count_1)

if count_0>count_1:
    print(count_1)
else:
    print(count_0)