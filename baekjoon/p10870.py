n = int(input())
dp = [0,1]

for i in range(2, n+1): 
    num = dp[i-1]+dp[i-2] 
    dp.append(num)
print(dp[n])


n = int(input())
def fibonacci(n):
    if n<=1:
        return n
    return fibonacci(n-1)+ fibonacci(n-2)

print(fibonacci(n))