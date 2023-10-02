import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())
arr=[[] for _ in range(n+1)]
visited=[False]*(n+1)

for _ in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)


def dfs(v):
    visited[e] = True
    for e in arr[v]:
        if not visited[e]:
            dfs(e)

ans=0
for i in range(1, n+1):
    if not visited[i]: 
        dfs(i)
        ans+=1

print(ans)