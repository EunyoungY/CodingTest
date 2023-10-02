import sys
from collections import deque
input = sys.stdin.readline
N, M, T = map(int, input().split())
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
m = [list(map(int, input().split())) for _ in range(N)]


def bfs():
    q = deque()
    visited = [[-1] * M for _ in range(N)]
    gram = sys.maxsize
    q.append((0, 0))
    visited[0][0] = 0
    while q:
        x, y = q.popleft() 
        if m[x][y] == 2:
            gram = visited[x][y] + N-1-x + M-1-y

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == -1:
                if m[nx][ny] == 0 or m[nx][ny] == 2:
                    visited[nx][ny] = visited[x][y]+1
                    q.append((nx, ny)) 
    return min(visited[x][y], gram)


res = bfs()
if res <= T:
    print(res)
else:
    print("Fail")

'''
3 3 100 
0 1 2 
0 1 1 
0 0 0
'''