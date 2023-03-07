#동전 0//동전의 조건이 특별해서 동적 프로그래밍보다 빠르게 답을 찾을 수 있는 문제
#그리디/탐욕 알고리즘-매트로이드(거스름 돈)//항상 최적 해
# n종류=입력받는 동전 가치//10종류=[1,5,10,50,100,500,1000,5000,10000,50000]
# k원 = 가치 합//4200원
import sys
n,k=map(int,sys.stdin.readline().split()) 
# n k 입력받기 
coin=[]
#동전 가치 배열로 입력받기
for i in range(n):
    c=int(sys.stdin.readline())#입력받으면 문자열>int로 변환
    coin.append(c)
#append : c를 coin array맨 끝에 추가하기

coin.sort(reverse=True)
#a1=[6,3,9] // a1.sort() =[3,6,9] //a1.sort(reverse=True)=[9,6,3]
#a1.reverse() =[9,3,6]
count=0
for i in coin:
    if k>i:
        count+=k//i #k/i의 몫 count
        k=k%i #k/i의 나머지 k
print(count)