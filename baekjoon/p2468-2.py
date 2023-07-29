import sys
sys.setrecursionlimit(10**6)
n = int(input())
arr = []
visited = [[False]*n for _ in range(n)]
highest = 0
for i in range(n):
    row = list(map(int, input().split()))
    arr.append(row) 
    highest = max(max(row), highest)
 
dx=[1,-1,0,0]
dy=[0,0,1,-1]

def dfs(x,y, k):
    visited[x][y] = True
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]            
        if 0<=nx<n and 0<=ny<n and arr[nx][ny] > k:
            if not visited[nx][ny]:  
                dfs(nx,ny, k)
            

answer=0

for height in range(highest+1):
    visited = [[False]*n for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] > height and not visited[i][j]:
                dfs(i,j, height)
                count += 1
    answer = max(answer, count)

print(answer)