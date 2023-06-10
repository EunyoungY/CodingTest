import sys
N = int(input())
A = []
sorted_A = []
for i in range(N):
    num = int(sys.stdin.readline())
    A.append((num, i))
sorted_A = sorted(A)

max = sorted_A[0][1]-A[0][1]
for i in range(N):
    if max < sorted_A[i][1]-A[i][1]:
        max = sorted_A[i][1]-A[i][1]

print(max+1)

'''
5
10
1
5
2
3

'''
