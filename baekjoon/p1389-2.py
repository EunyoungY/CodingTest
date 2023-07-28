import sys
from collections import deque

n, m = map(int, input().split())
arr = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

 
q = deque()

def bfs(v):
    visited= [False]*(n+1)
    distance= [0]*(n+1)
    q.append(v)
    visited[v] = True
    while q:
        now = q.popleft()
        for a in arr[now]:
            if not visited[a]:
                q.append(a)
                visited[a] = True
                distance[a] = distance[now]+1 
    return sum(distance)
    
    
kevins = [] 
for i in range(1, n+1):
    kevins.append(bfs(i))
print(kevins.index(min(kevins))+1)