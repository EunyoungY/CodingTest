dp = [[[0]*100001 for _ in range(5)] for _ in range(5)]
# dp = [[[0]*3 for _ in range(3)] for _ in range(3)]
# print(dp)

arr = []
while True:
    n = int(input())
    if n == 0:
        break
    arr.append(n)

for k in range(arr):
    for i in range(5):
        for j in range(5):
            # 왼쪽에서 왔을 경우
            dp[k][i][j] = dp[n-1][i-1][j] + min()
