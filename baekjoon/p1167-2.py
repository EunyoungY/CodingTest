from collections import deque

n = int(input())
arr = [[] for _ in range(n+1)]

for i in range(1, n+1):
    row = list(map(int, input().split()))
    for j in range(1, len(row)-2, 2):
        arr[i].append((row[j], row[j+1]))

print(arr)


def bfs(v):
    dis = [0]*(n+1)
    visited = [False]*(n+1)
    q = deque()
    q.append(arr[v][0])
    visited[v] = True

    while q:
        now = q.popleft()
        for a in arr[now[0]]:
            if not visited[a[0]]:
                visited[a[0]] = True
                dis[a[0]] += now[1] +a[1]
                q.append(a)
    print("dis", dis)


bfs(1)
