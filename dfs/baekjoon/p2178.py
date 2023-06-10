import sys
from collections import deque

n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(int, input())))
# 여기에 10분씀

def bfs():
    q = deque()
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    q.append([0,0])
    while q:
        now = q.popleft()
        x = now[0]
        y = now[1]
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 1:
                arr[nx][ny] = arr[x][y]+1
                # q.append(arr[nx][ny])
                q.append([nx, ny])


bfs()
print(arr[n-1][m-1]) 