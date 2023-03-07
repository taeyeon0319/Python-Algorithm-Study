import sys
input=list(sys.stdin.readline().rstrip())
column=int(ord(input[0]))-96
row=int(input[1])
#print(input)
#print(row)
#print(column)
move=[(-2,1),(-2,-1),(2,1),(2,-1),(-1,2),(1,2),(-1,-2),(1,-2)]
result=0
for i in move:
    nrow=row+i[0]
    ncolumn=column+i[1]
    if nrow>=1 and nrow<=8 and ncolumn>=1 and ncolumn<=8:
        result+=1
print(result)
