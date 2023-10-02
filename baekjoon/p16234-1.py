from collections import deque
import sys
input = sys.stdin.readline

n, l, r = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*n for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(a, b):
    q = deque()
    temp = deque()
    visited[a][b] = True
    q.append((a, b))
    temp.append((a, b))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < n and 0 <= ny < n and l <= abs(board[nx][ny]-board[x][y]) <= r and not visited[nx][ny]:
                q.append((nx, ny))
                temp.append((nx, ny))
                visited[nx][ny] = True
    return temp


cnt = 0
while True:
    flag = 0
    
    visited = [[False]*n for _ in range(n)] 
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                united = bfs(i, j)
                if len(united) > 1:
                    flag = 1
                    pop = sum(board[x][y] for x, y in united)//len(united)
                    for x, y in united:
                        board[x][y] = pop
    if flag == 0:
        print(cnt)
        break
    cnt += 1
