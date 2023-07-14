n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))

dp = [1]+[0]*(k)
for coin in coins:
    for sumVal in range(coin,k+1):
        dp[sumVal] += dp[sumVal-coin]
# print(dp)
print(dp[k])
