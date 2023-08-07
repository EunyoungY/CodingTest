import sys
sys.setrecursionlimit(10**6)
n = int(input()) #num of computers
k = int(input())
arr=[[] for _ in range(n+1)]
for _ in range(k):
    a,b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

# print(arr)

visited=[False]*(n+1)
cnt = 0
def dfs(v):
    global cnt 
    
    visited[v] = True
    for a in arr[v]:
        if not visited[a]:
            cnt+=1
            dfs(a)

dfs(1)
print(cnt)