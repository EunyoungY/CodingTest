n = int(input())
arr = list(map(int, input().split()))

arrLen = len(arr)-1
dp = [[0]*21 for _ in range(arrLen)]
dp[0][arr[0]] = 1

for h in range(arrLen-1):
    for w in range(21):
        if dp[h][w] > 0:
            if 0 <= w-arr[h+1] <=20:
                dp[h+1][w-arr[h+1]] += dp[h][w]
            if 0 <= w+arr[h+1] <=20:
                dp[h+1][w+arr[h+1]] += dp[h][w]

# for i in range(n-1):
#     print(dp[i])
    
print(dp[-1][arr[-1]])
                