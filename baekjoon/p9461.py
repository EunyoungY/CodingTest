n = int(input())
dp = [0 for _ in range(101)]

dp[0]=1
dp[1]=1
dp[2]=1
dp[3]=2
dp[4]=2
#li = [1,1,1,2,2]
for i in range(5, 101):
    dp[i] = dp[i-1]+dp[i-5]

for _ in range(n):
    num = int(input())
    print(dp[num-1])
    
