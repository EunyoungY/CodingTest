import sys
intput = sys.stdin.readline
n, k = map(int, input().split())
A = []
for _ in range(n):
    A.append(int(input()))

A.sort(reverse=True)

count = 0
for i in A:
    if i <= k:
        count += int(k/i)
        k = k % i

print(count)

'''
10 4200
1
5
10
50
100
500
1000
5000
10000
50000
'''
