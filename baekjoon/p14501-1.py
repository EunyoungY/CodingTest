n = int(input())
T, P = [], []
for i in range(n):
    t, p = map(int,input().split())
    T.append(t)
    P.append(p)

dp=[0]*(n+1)

for i in range(n-1, -1, -1):
    if i+T[i]>n:
        dp[i] =dp[i+1]
    else:
        dp[i] = max(dp[i+1], P[i]+dp[i+T[i]])

print(dp[0])