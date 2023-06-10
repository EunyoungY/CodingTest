'''
n, m = map(int, input().split())
list = list(map(int, input().split()))
subSum = []
print(subSum)
count = 0
for i in range(len(list)):
    for j in range(len(list)):
        if i <= j:
            if i == j:
                subSum[i-1][j-1] = list[i-1]

            else:
                subSum[i-1][j-1] = subSum[i-1][j-2]+list[j]

            if subSum[i-1][j-1] % 3 == 0:
                count = count+1

print(count)
'''
