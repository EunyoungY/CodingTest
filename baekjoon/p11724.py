import sys
sys.setrecursionlimit(100000) #해당 줄 안 넣었더니 런타임에러(RecursionError) 발생
input = sys.stdin.readline #해당 줄 안 넣었더니 시간 초과 발생
n, m = map(int, input().split())
arr = [[] for _ in range(n+1)]
visited = [False] * (n+1)
for _ in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

def dfs(v):
    global arr
    visited[v] = True
    for i in arr[v]:
        if not visited[i]:
            dfs(i)

count = 0
for i in range(1, n+1):
    if not visited[i]:
        dfs(i)
        count += 1
print(count)

'''
6 5
1 2
2 5
5 1
3 4
4 6
=>2
'''
