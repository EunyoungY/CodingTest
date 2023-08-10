'''
cnt = 0
 bfs
 q에 1인애들 먼저 넣어놓고
 
전체 돌면서 0이 있으면 -1 출력하고 바로 종료
0이 없으면 cnt출력
'''
from collections import deque
m, n, h = map(int, input().split())
arr = [[] for _ in range(h)]
q = deque()

for i in range(h):
    for j in range(n):
        arr[i].append(list(map(int, input().split())))
        for k in range(m):
            if arr[i][j][k] == 1: 
                q.append([i, j, k])  # h, n, m

dx = [0, 0, 1, -1, 0, 0]
dy = [0, 0, 0, 0, 1, -1]
dz = [1, -1, 0, 0, 0, 0]


cnt = [[[0]*m for _ in range(n)] for _ in range(h)]


def bfs():
    while q:
        z, y, x = q.popleft()
        for i in range(6):
            nz, ny, nx = z+dz[i], y+dy[i], x+dx[i]
            if 0 <= nx < m and 0 <= ny < n and 0 <= nz < h and arr[nz][ny][nx] == 0:
                arr[nz][ny][nx] = 1
                q.append([nz, ny, nx])
                cnt[nz][ny][nx] = cnt[z][y][x]+1


bfs()

ans = 0
for i in range(h):
    for j in range(n):
        for k in range(m):
            ans = max(ans, cnt[i][j][k])
            if arr[i][j][k] == 0:
                print(-1)
                exit()

print(ans)
''' 
5 3 2
0 0 0 0 0
0 0 0 0 03
0 0 0 0 0
0 0 0 0 0
0 0 1 0 0
0 0 0 0 0
'''
