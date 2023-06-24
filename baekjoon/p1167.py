
'''
가장 깊은 depth를 찾을 때, 어떤 algorithm을 쓸까? DFS/ BFS? => DFS선택

구상 30분
'''
 
import sys
n = int(input())
arr = [[] for _ in range(n+1)]
visited = [False] * (n+1)
distance = [0] * (n+1)

for i in range(n):
    row = list(map(int, input().split()))
    for i in range(1, len(row)-1, 2):
        arr[row[0]].append([row[i], row[i+1]])

def dfs(v, depth):
    visited[v] = True
    distance[v] = depth
    for a in arr[v]:
        if not visited[a[0]]:
            dfs(a[0], depth+a[1])
    visited[v] = False


dfs(1, 0)
x = distance.index(max(distance))
distance = [0] * (n+1)
dfs(x, 0)
print(max(distance))
'''
입력 40분
1) list에 한 줄을 넣은 후 처리
2) -1나오기 전까지 쌍으로 처리

나머지 구현 10분
'''
