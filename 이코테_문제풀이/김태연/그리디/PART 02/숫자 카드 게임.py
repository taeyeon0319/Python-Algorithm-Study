n, m = map(int, input().split())
result = 0

for i in range(n):
    num_list = list(map(int, input().split()))
    min_value = min(num_list)
    result = max(result, min_value)
print(result)

