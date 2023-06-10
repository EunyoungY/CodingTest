# top down
# n = int(input())
# D = [-1]*(n+1)

# D[1] = 0

# def func(n):
#     if D[n] != -1:
#         return D[n]
#     if n % 2 == 0 and n % 3 == 0:
#         D[n] = min(func(n//2), func(n//3))+1
#     elif n % 2 == 0:
#         D[n] = min(func(n//2), func(n-1))+1
#     elif n % 3 == 0:
#         D[n] = min(func(n//3), func(n-1))+1
#     else:
#         D[n] = func(n-1)+1
#     return D[n]
# func(n)
# print(D[n])

# bottom up
n = int(input())
D = [-1]*(n+1)
D[1] = 0
A = [-1]*(n+1)
A[1] = 0 

for i in range(2, n+1):
    D[i] = D[i-1]+1
    A[i] = A[i-1]+1
    if i % 2 == 0:
        D[i] = min(D[i-1]+1, D[i//2]+1)
        A[i] = min(A[i], A[i//2]+1)
    if i % 3 == 0:
        D[i] = min(D[i-1]+1, D[i//3]+1)
        A[i] = min(A[i], A[i//3]+1) 
# print(D[n])
print(A[n])

# for i in range(2, (n+1)):
#     # if n % 6 == 0:
#     #     D[i] = min(D[i//2], D[i//3], D[i-1])+1
#     # if (n % 2 != 0 and n % 3 != 0):
#     #     D[i] = D[i-1]+1
#     if n % 3 == 0:
#         D[i] = min(D[i-1], D[i//3])+1
#     if n % 2 == 0:
#         D[i] = min(D[i-1], D[i//2])+1
#     else:
#         D[i] = D[i-1]+1

# print(D[i])
