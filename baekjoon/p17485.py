import sys
INF = 1000000
input = sys.stdin.readline
height, width = map(int, input().split())
board = []
for _ in range(height):
    board.append(list(map(int, input().split())))
dp = [[[sys.maxsize]*3 for _ in range(width)] for _ in range(height)]


for i in range(height):
    for j in range(width):
        for k in range(3):
            if i == 0:
                dp[i][j][k] = board[i][j] 
            else:
                if (j == 0 and k == 2) or (j == width-1 and k == 0):
                    continue
                if k == 0:
                    dp[i][j][k] = min(dp[i-1][j+1][1], dp[i-1]
                                      [j+1][2])+board[i][j]
                elif k == 1:
                    dp[i][j][k] = min(dp[i-1][j][0], dp[i-1][j][2])+board[i][j]
                else:
                    dp[i][j][k] = min(dp[i-1][j-1][0], dp[i-1]
                                      [j-1][1])+board[i][j]
                    
res = sys.maxsize
for i in range(width):
    res = min(min(dp[height-1][i]), res)
print(res)
