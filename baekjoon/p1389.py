import sys
from collections import deque
n, m = map(int, input().split())
arr = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    if b not in arr[a]:
        arr[a].append(b)
    if a not in arr[b]:
        arr[b].append(a)

distance = [5000] * (n+1)
visited = [False] * (n+1)

kevins = [5000] * (n+1)
def dfs(v, depth):
    visited[v] = True
    for i in arr[v]:
        if not visited[i]:
            visited[i] = True
            distance[i] = min(distance[i], depth)
            dfs(i, depth+1) 
    visited[v] = False            

for i in range(1, n+1):
    dfs(i, 1)
    kevin = sum(distance)-10000
    kevins[i] = kevin
    distance = [5000] * (n+1) #distance 초기값을 [0]으로 해서 자꾸 에러남

print(kevins.index(min(kevins)))

 

