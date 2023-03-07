import sys
n,m = map(int,sys.stdin.readline().split())
array=[]
for i in range(n):#array.append(x): 새로운 요소를 array끝에 추가
    array.append(list(map(int,sys.stdin.readline().split())))
#print(array)
row_min=[]
for i in range(n):
    row_min.append(min(array[i]))
#print(row_min)
print(max(row_min))

