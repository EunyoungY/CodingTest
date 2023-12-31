n = int(input())

T, P = [], []
dp = [0]*(n+1)

for _ in range(n):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

# #Top Down
# for i in range(n-1, -1, -1):
#     if i+T[i] >n:
#         dp[i] = dp[i+1]
#     else: 
#         dp[i] = max(dp[i+1], dp[i+T[i]]+P[i]) 
# print(dp[0])

#Bottom Up
for i in range(n):
    for j in range(i+T[i], n+1):   
        if dp[j] < dp[i]+P[i]:
            dp[j] = dp[i]+P[i] 
print(dp[-1])