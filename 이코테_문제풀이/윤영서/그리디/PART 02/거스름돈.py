import sys
n=int(sys.stdin.readline())
count=0
coin=[500,100,50,10]
for i in coin:
    #n=n%i
    count+=n//i
    n=n%i
    #순서 바꿔서 틀림:
    # n=n%i  
    # count+=n//i 이면 위에서 n값이 바뀜
    

print(count)


