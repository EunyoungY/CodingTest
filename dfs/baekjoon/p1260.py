import sys
from collections import deque

n, m, v = map(int, input().split())
arr = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

for a in arr:
    a.sort()

visited = [False] * (n+1)


def dfs(v):
    visited[v] = True
    print(v, end=' ')
    for i in arr[v]:
        if not visited[i]:
            dfs(i)

def bfs(v):
    q = deque()
    q.append(v)
    visited[v] = True
    while q:
        now = q.popleft()
        print(now, end=' ')
        for i in arr[now]:
            if not visited[i]:
                visited[i] = True #
                q.append(i)

dfs(v)
print()
visited = [False] * (n+1)
bfs(v)


