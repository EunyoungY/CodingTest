#구현: 13분
#도움 : Yes
#시간초과
import sys
import math
n = int(input())

def isPrime(num):
    # for i in range(2, num):  #시간초과
    for i in range(2, int(math.sqrt(num))+1):
        if num%i == 0:
            return False
    return True

def dfs(v):
    if len(str(v))>=n:
        print(v)
        return
    for i in [1,3,5,7,9]:
        if isPrime(v*10+i) == True:
            dfs(v*10+i)

dfs(2)
dfs(3)
dfs(5)
dfs(7)
'''
구상 15분
맨 앞자리
2,3,5,7

왼쪽에서 두번째 자리
1,3,5,7,9 중에서 맨 앞자리와 합쳐서 소수인지 판별

dfs

입력
isPrime(소수판별함수)
dfs(v):
    if depth == 4:
        print & return7
    for i in 1,3,5,7,9
        if v*10+i == 소수
            dfs(v*10+i)

dfs(2)
dfs(3)
dfs(5)
dfs(7)
'''

