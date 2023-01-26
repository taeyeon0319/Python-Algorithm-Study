num = list(map(int, input()))
f=0
b=0

for i in range(0, int(len(num)/2)):
    f+=num[i]
    b+=num[-(i+1)]

if f==b:
    print("LUCKY")
else:
    print("READY")