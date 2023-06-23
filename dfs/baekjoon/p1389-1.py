import sys

n, m = map(int, input().split())

arr=[[] for _ in range(n+1)]
visited = [False]*(n+1)
distances = [100]*(n+1)

def dfs(v, depth):
    visited[v] = True
    distances[v] = min(depth, distances[v])
    for a in arr[v]:
        if not visited[a]:
            visited[a] = True
            dfs(a, depth+1)
    visited[v] = False
    
for _ in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

answers = []
for i in range(1, n+1):
    distances = [100]*(n+1)
    dfs(i, 0) 
    answers.append(sum(distances))
 
print(answers.index(min(answers))+1)

'''
Key Idea: 각각의 노드 사이의 최소값 구하기
BFS: bfs로 풀면 가장 근접한 이웃 먼저 탐색을 하기 때문에 distance[v]값이 항상 최소가 됨
DFS: dfs로 풀면 distance[v]값을 항상
'''
    