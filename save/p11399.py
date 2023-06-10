import sys
n = int(input())
a = list(map(int, sys.stdin.readline().split()))

for i in range(1, n):
    key = i
    for j in range(i-1, -1, -1):
        if a[key] < a[j]:
            temp = a[j]
            a[j] = a[key]
            a[key] = temp 
        key = key-1

sum = a[0]
result = [0]*n
result[0] = a[0]

for i in range(1, n):
    result[i] = result[i-1]+a[i]
    sum = sum+result[i]
print(sum)

'''
5
3 1 4 3 2
'''
