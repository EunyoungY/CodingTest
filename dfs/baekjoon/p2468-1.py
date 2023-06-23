'''
높이 (0~h)에 대해 h를 초과 하는 숫자들 군집의 개수
= 연결된 요소 group의 총 개수 구하기
'''

import sys
sys.setrecursionlimit(10**6)
n = int(input())
arr = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
visited=[[False]*n for _ in range(n)]

max_height = 0
for i in range(n):
    row = list(map(int, input().split()))
    arr.append(row)
    for num in row:
        if num > max_height:
            max_height = num


def dfs(a, b,height): 
    visited[a][b] = True
    x,y=a,b 
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<n and 0<=ny<n and arr[nx][ny]>height and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx,ny, height) 

answer = 0
for height in range(max_height):
    visited=[[False]*n for _ in range(n)]
    count=0
    for i in range(n):
        for j in range(n):
            if arr[i][j] > height and not visited[i][j]:
                dfs(i, j, height)
                count+=1 
    answer=max(answer, count)
print(answer)