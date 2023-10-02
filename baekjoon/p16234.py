from collections import deque
n, l, r = map(int, input().split())
arr=[]
for _ in range(n):
    line = list(map(int, input().split()))
    arr.append(line)

dx=[1,-1,0,0]
dy=[0,0,1,-1]
visited = [[False]*n for _ in range(n)]
blocked = 1
ans = 0
def bfs(a, b): 
    q = deque()
    q2 = deque()
    q.append((a,b))
    q2.append((a, b))
    visited[a][b] = True 
    while q: 
        x, y = q.popleft() 
        for i in range(4): 
            nx = x+dx[i]    
            ny = y+dy[i] 
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
                if l<=abs(arr[nx][ny]-arr[x][y]) <=r:
                    visited[nx][ny] = True
                    q.append((nx,ny)) 
                    q2.append((nx, ny)) 
    return q2
   
            
    
while True:
    visited = [[False]*n for _ in range(n)]
    flag = 0     
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                country = bfs(i,j) 
                if len(country)>1:
                    flag = 1
                    population = sum(arr[x][y] for x,y in country)//len(country)
                    for x,y in country:
                        arr[x][y] = population
    if flag == 0:
        break
    ans+=1 
print(ans)

'''
1. bfs 안에서 flag=1이후 부분을 해결하려고 했음. bfs라는 함수의 쓰임에 맞게끔 해당 로직만 짜기
2. while문의 종료 조건을 잘못 생각했음(사실 이것 때문에 flag=1에 해당하는 부분을 bfs안에서 하려고함)
*. sum(arr[x][y] for x,y in country)
'''