import sys
input = sys.stdin.readline
N = int(input())
# D = [0]*(N+1)
D = [0]*(1001)

D[1] = 1
D[2] = 2 
'''D = [0]*(N+1)로 하면 N=1일 때, D[2]=2하는 순간 index out of range가 나기 때문에 범위를 늘려야 함'''

for i in range(3, N+1):
    # D[i] = D[i-1] + D[i-2]
    D[i] = (D[i-1] + D[i-2])%10007

# print(D[N] % 10007)
print(D[N])


'''
D[i] = 2*i 크기 직사각형을 채우는 방법의 수
D[1] = 1
D[2] = 2
D[3] = 3 D[2]+D[1]
D[4] = 6

Output = D[n]%10007 
'''
