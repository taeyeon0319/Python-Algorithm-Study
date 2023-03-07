for l in range(24):
    print(l)
    N=l
    N3=0
    if N>=3:
        N3=(N-3)//10+1
        N-=N3
    N+=1
    h=l
    count=0
    for i in range(h+1):
        for j in range(60):
            for k in range(60):
                if '3' in str(i)+str(j)+str(k):#시,분,초
                    count+=1
    print(N*1575+N3*3600,count)