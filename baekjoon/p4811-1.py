import sys
input = sys.stdin.readline
dp = [[0]*31 for _ in range(31)]

for i in range(0, 31):
    dp[i][0] = 1
    
for j in range(1, 31):
    for i in range(30):
        if i==0:
            dp[i][j] = dp[i+1][j-1]
        else:
            dp[i][j] = dp[i-1][j]+dp[i+1][j-1]
# print(dp)
while True:
    N = int(input())
    if N == 0:
        break
    print(dp[0][N])
# for 

'''
6
1
4
2
3
30
0
'''
