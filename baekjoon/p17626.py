import math

n = int(input())
dp = [0,1]

for i in range(2, n+1):
    min_value = 500000
    
    for j in range(1, int(math.sqrt(i))+1):
        min_value = min(min_value, dp[i-j**2])
    dp[i].append(min_value+1)
print(dp[n])