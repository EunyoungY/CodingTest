t = int(input())
arr=[]
max_val = 0
for _ in range(t):
    n,m = map(int,input().split())
    arr.append([n,m])
    max_val = max(max_val, m)

dp=[1,1]
for i in range(2, max_val+1):
    num = dp[i-1]*i
    dp.append(num) 
for n, m in arr:
    print((dp[m]//dp[n])//dp[m-n])
 