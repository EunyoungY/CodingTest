import sys
N = int(sys.stdin.readline())
A = [0]*N

for i in range(N):
    A[i] = int(input())

for i in range(0, N-1):
    for j in range(0, N-1-i):
        if A[j] > A[j+1]:
            temp = A[j]
            A[j] = A[j+1]
            A[j+1] = temp
for i in range(N):
    print(A[i])

'''
5
5
2
3
4
1
'''
