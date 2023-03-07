n, m, k = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
first = num[n-1]
second = num[n-2]

result = 0
count = k

while m != 0:
    if count > 0:
        result += first
        count-=1
        m-=1
    elif count>-1:
        result += second
        m-=1
        count=k
        

print("{}".format(result))

# == 모범답안 ==
n, m, k = map(int, input().split())
num = list(map(int, input().split()))

num.sort()
first = num[n-1]
second = num[n-2]

count = (m//(k+1))*k
count +=m%(k+1)

result=0
result += (count) * first
result += (m-count) * second

print(result)
