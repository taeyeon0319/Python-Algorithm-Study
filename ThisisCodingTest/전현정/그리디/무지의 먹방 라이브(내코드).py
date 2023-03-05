#que를 활용하여 k+1번째 음식의 index를 찾도록 한 코드
#효율성 테스트를 통과하지 못함.(시간 초과)
from collections import deque

def solution(food_times, k):
    if sum(food_times)<=k:
        answer=-1
    else:
        que=deque()
        for i in range(len(food_times)):
            que.append([i+1,food_times[i]])
        
        for i in range(k):
            temp=que.popleft()
            temp[1]-=1
            if temp[1]>0:
                que.append(temp)
                
        ans=que.popleft()
        answer=ans[0]
    return answer