#회의실 배정// N개 회의 수 : (s시작시간,e끝나는 시간)
# 가능한 한 많은 구간을 선택하는 문제
import sys
N = int(sys.stdin.readline())
time = [[0]*2 for _ in range(N)]
#[[0]*n for_in range(m)] // [[0]*n]*m 차이점 
#a=[[0]*2]*3 // a[0][0]=1 // print(a) 
# >>[[1,0],[1,0],[1,0]] : 각각 배열 선언

# b=[[0]*2 for_in range(3)] // b[0][0]=1 // print(b) 
# >> [[1,0],[0,0],[0,0]] : 2차원 배열 선언
for i in range(N):
    s, e = map(int, sys.stdin.readline().split())
    time[i][0] = s
    time[i][1] = e

time.sort(key = lambda x: (x[1], x[0]))
#lambda람다 함수 
#e = sorted(a, key = lambda x : (x[0], -x[1])) //x[0]오름차순,x[1]내림차순
#time 배열을 x[1]오름차순, x[0]오름차순
cnt = 1
end_time = time[0][1]
#끝나는 시간이 가장 작은 쌍의 끝나는 시간
for i in range(1, N):#1부터 N-1까지//0부터니까
    if time[i][0] >= end_time:
        cnt += 1
        end_time = time[i][1]
#시작시간이 가장 짧은 쌍
print(cnt)