from collections import deque
import sys
input = sys.stdin.readline

N = int(input()) #큐스택을 구성하는 자료구조의 개수 
dst_list = list(map(int,input().split())) #자료구조 입력받기
dst_data = list(map(int,input().split())) #데이터 입력받기
M = int(input())
C = list(map(int,input().split())) #삽입할 원소 C 


q = deque()

for idx , d in enumerate(dst_list):
    if d == 0 : #만일 큐라면 원소 추가 
        q.append(dst_data[idx])


for c in C :
    q.appendleft(c) 
    x = q.pop() 
    print(x , end = " ")