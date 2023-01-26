def solution(food_times, k):
    answer = 0
    for i in range(k):
        if i<len(food_times):
            if(food_times[i]!=0):
                food_times[i] -= 1
            else:
                food_times[i+1] -= 1
        else:
            if(food_times[i-len(food_times)]!=0):
                food_times[i-len(food_times)] -= 1
            else:
                food_times[i-len(food_times)+1] -= 1
    answer = i+1
    return answer

food_times = list(map(int, input().split()))
k = int(input())

print(solution(food_times, k))