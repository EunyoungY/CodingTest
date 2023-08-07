n, m, r = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))


ans = [[0]*m for _ in range(n)]
layer = min(n, m)//2
for i in range(0, layer):
    lst = []
    for j in range(i, m-i):  # 위
        lst.append(arr[i][j])
    for j in range(i+1, n-i-1):  # 오
        lst.append(arr[j][n-i-1])
    for j in range(i, m-i):  # 아
        lst.append(arr[n-1-i][n-j-1])
    for j in range(n-1, i+1, -1):  # 왼
        lst.append(arr[j-i-1][i])
 
    r = r % len(lst)
    new = lst[r:]+lst[:r] 
    cnt = 0
    
    for j in range(i, m-i):  # 위
        ans[i][j] = new[cnt]
        cnt+=1 
    for j in range(i+1, n-i-1):  # 오
        ans[j][m-i-1] = new[cnt]
        cnt+=1 
    for j in range(i, m-i):  # 아
        ans[n-1-i][n-j-1] = new[cnt]
        cnt+=1 
    for j in range(n-1, i+1, -1):  # 왼
        ans[j-i-1][i] = new[cnt]
        cnt+=1 
 
for line in ans:
    print(*line)
 
