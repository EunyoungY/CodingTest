import sys
sys.setrecursionlimit(10**6)

n = int(input())
arr=[[] for _ in range(n+1)]

for i in range(n-1):
    a,b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

lst=[0]*(n+1)
def dfs(v):     
    for a in arr[v]:
        if lst[a] == 0:
            lst[a] = v
            dfs(a)

dfs(1)

for i in range(2, n+1):
    print(lst[i])
