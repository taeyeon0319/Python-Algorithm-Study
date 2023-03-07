import sys
text=sys.stdin.readline().strip()
result=0
for i in text:
    temp=int(i)
    if temp==0:
        continue
    elif temp==1:
        result+=1
    else:
        if result==0:
            result+=temp
        else:
            result*=temp
print(result)