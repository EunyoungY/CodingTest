from collections import deque
import sys
n, m = map(int, input().split())
A = [[0]*m for _ in range(n)]
visited = [[False]*m for _ in range(n)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


for i in range(n):
    numbers = list(input())
    for j in range(m):
        A[i][j] = int(numbers[j])


def BFS(a, b):
    queue = deque()
    queue.append((a, b))
    visited[a][b] = True
    while queue:
        now = queue.popleft()
        for i in range(4):
            x = now[0]+dx[i]
            y = now[1]+dy[i]
            if x >= 0 and y >= 0 and x < n and y < m:
                if not visited[x][y] and A[x][y] == 1:
                    A[x][y] = A[now[0]][now[1]] + 1
                    queue.append((x, y))
                    visited[x][y] = True


BFS(0, 0)
print(A[n-1][m-1])

'''
4 6
101111
101010
101011
111011
'''
