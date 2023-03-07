n = int(input())
m = list(map(int, input().split()))
group = 0
member = 0

m.sort()

for i in m:
    member += 1
    if member>=i:
        group += 1
        member=0
print(group)

