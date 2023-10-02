import sys
from collections import deque

n, m, t = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def bfs():
    visited = [[sys.maxsize]*m for _ in range(n)]
    q = deque()
    gram = visited[n-1][m-1]
    visited[0][0] = 0
    q.append((0, 0))

    while q:
        x, y = q.popleft()
        if board[x][y] == 2:
            gram = visited[x][y]+(n-1-x) + (m-1-y)
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] != 1 and visited[nx][ny] > visited[x][y]+1:
                visited[nx][ny] = visited[x][y]+1
                q.append((nx, ny))
    return min(gram, visited[n-1][m-1])


time = bfs()
if time <= t:
    print(time)
else:
    print('Fail')
