n = int(input())
dp=[0,1,2]

for i in range(3, n+1):
    num = (dp[i-1]+dp[i-2])%10007
    dp.append(num)

print(dp[n])
