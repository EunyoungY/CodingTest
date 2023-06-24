import sys
from collections import deque

n, m = map(int, input().split())
arr = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

def bfs(v):
    q = deque()
    q.append(v)
    visited = [False] * (n+1)
    visited[v] = True
    depth = [0] * (n+1)
    while q:
        now = q.popleft()
        for i in arr[now]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
                depth[i] = depth[now]+1
    return depth

kevins = []
for i in range(1, n+1):
    kevins.append(sum(bfs(i)))
print(kevins.index(min(kevins))+1)
