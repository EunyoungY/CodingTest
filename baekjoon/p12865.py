n, k = map(int, input().split())

knapsack = [[0]*(k+1) for _ in range(n+1)]
for i in range(1, n+1):
    weight, value = map(int, input().split())
    for j in range(1, k+1):
        if j < weight:
            knapsack[i][j] = knapsack[i-1][j]
        else:
            knapsack[i][j] = max(knapsack[i-1][j], knapsack[i-1][j-weight]+value)
            
# print(*knapsack)
print(knapsack[n][k])

'''
4 7
6 13
4 8
3 6
5 12
'''