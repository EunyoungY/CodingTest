'''Dynamic Programming(DP)'''
import sys
input = sys.stdin.readline
N = int(input())
D = [0]*(N+1)  # 개수 주의
D[1] = 0

for i in range(2, N+1):  # 범위 주의
    D[i] = D[i-2]+1
    if(i % 2 == 0):
        D[i] = min(D[i], D[i//2]+1)
    if(i % 3 == 0):
        D[i] = min(D[i], D[i//3]+1)

print(D[N])
'''
[step 1]
D[1] = 0
D[2] = 1 
OUTPUT: 연산을 사용하는 횟수의 최솟값
D[i]: i에서 1로 만드는데 걸리는 최소 연산 횟수
D[i] = D[i-2]+1
if(i%2==0) D[i] = min(D[i], D[i/2]+1)
if(i%3==0) D[i] = min(D[i], D[i/3]+1)

[step 2]
N: 구하고자 하는 수
D: dp table
D[1] = 0
for 2~N:
    식 반복해서 계산
print D[N]
'''
