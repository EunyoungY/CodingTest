import sys
n = int(input())

dp = [0 for _ in range(n+2)]

dp[1] = 1
dp[2] = 2

for i in range(3, n+1):
    dp[i] = (dp[i-2]+dp[i-1]) %15746
print(dp[n])

# def find(num):
#     if num == 0:
#         return 0
#     elif num == 1:
#         return 1
#     elif num == 2:
#         return 2
#     else :
#         return find(num-1)+find(num-2)
# print(find(n))
