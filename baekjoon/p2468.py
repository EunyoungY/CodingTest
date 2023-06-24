'''
Plan 12mins
2<=n<=100
1<=max_height<=100
safes = [] * (max_height+1)
for i in range(1, max_height+1):
    for j in range(n):
        for k in range(n)
O(100*n^2) = O(1,000,000)

핵심!!!!!!!!!2차원 배열 돌아다니며 연결요소의 개수 찾기
'''
#implementation: 60m

import sys
from collections import deque

n = int(input())
arr = []
height = 0

for i in range(n):
    arr.append(list(map(int, input().split())))
    for num in arr[i]:
        if num>height:
            height = num
            
visited = [[False]*n for _ in range(n)]  # *************************** 
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
waters = []

def bfs(a,b, water):
    q = deque()
    q.append([a,b])
    visited[a][b] = True
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            # M: visited 안 넣어서 무한반복에 갇힘
            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny]>water and not visited[nx][ny]:
                q.append([nx,ny])
                visited[nx][ny] = True  

for water in range(height):
    area = 0
    for j in range(n):
        for k in range(n):
            if not visited[j][k] and arr[j][k] > water:
                bfs(j,k, water)
                # M if arr[j][k] >= 5:
                area += 1
    visited = [[False]*n for _ in range(n)]
    waters.append(area)
print(max(waters))

 