import sys
input = sys.stdin.readline
n, m = map(int, input().split())
board = [list((map(int, input().rstrip()))) for _ in range(n)]

ans = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 1 and j > 0 and i > 0:
            board[i][j] = min(board[i-1][j], board[i]
                              [j-1], board[i-1][j-1]) + 1
        ans = max(board[i][j], ans)
print(ans*ans)
