# dp = [0]*11
# dp[1] = 1
# dp[2] = 2
# dp[3] = 4

# for i in range(4, 11):
#     dp[i] = dp[i-1]+dp[i-2]+dp[i-3]

# n = int(input())
# for i in range(n):
#     n = int(input())
#     print(dp[n])

import sys
input = sys.stdin.readline
n = int(input())

dp = [0]*11 
dp[1] = 1
dp[2] = 2
dp[3] = 4

def n_sum(n):
    if dp[n]>0:
        return dp[n]
    dp[n] = n_sum(n-1)+n_sum(n-2)+n_sum(n-3)
    return dp[n]
# def n_sum(n):
#     if dp[n]>0:
#         return dp[n]
#     if n == 1:
#         dp[n] = 1
#     elif n == 2:
#         dp[n] = 2
#     elif n == 3:
#         dp[n] = 4
#     else:
#         dp[n] = n_sum(n-1)+n_sum(n-2)+n_sum(n-3)
#     return dp[n]


n_sum(10)
 
for i in range(n): 
    number = int(input())
    print(dp[number])


