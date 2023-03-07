import heapq

def solution(food_times, k):
    
  # 전체 음식을 다 먹는 시간이 k보다 작거나 같으면 모든 음식을 다 먹었으므로 -1반환
  if sum(food_times)<=k:
    return -1
  
  # 우선순위큐(최소힙)에다가 삽입
  # 음식 번호와 시간을 튜플형태로 삽입, 시간을 기준으로 최소힙 완성됨
  q=[]
  for i in range(len(food_times)):
    heapq.heappush(q, (food_times[i],i+1))
  
  
  foods = len(food_times) # 남은 음식의 개수
  previous = 0 # 이전 음식을 먹는데 걸리는 시간
  while True:
    # 남은 음식의 개수 * 음식을 먹는 시간 = 이 음식을 다 먹을 때까지 걸리는 시간
    now = q[0][0] # 여기서 pop을 하면 q에 아무것도 안남아서 마지막에 정렬이 안됨
    t=foods*(now-previous) # 한 음식을 다 먹어서 빼면 튜플에 남아있는 음식을 먹기위해 걸리는 시간이 줄어들어야함
    if k>=t:
      k-=t
      foods-=1
      previous = heapq.heappop(q)[0] # now와 같은 값이지만 여기서 pop을 함
    else:
      i = k%foods
      q.sort(key=lambda x:x[1]) # 음식 번호로 정렬
      return q[i][1]