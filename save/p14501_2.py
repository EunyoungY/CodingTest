

import sys
input = sys.stdin.readline
n = int(input())
# n일까지 벌 수 있는 최대수익을 저장,
d = [0]*20
tplist = [[0, 0]]
for _ in range(n):
    t, p = map(int, input().split())
    tplist.append([t, p])

for i in range(1, n+1):
    x = tplist[i][0]-1
    d[i] = max(d[i-1], d[i])
    d[i+x] = max(d[i-1]+tplist[i][1], d[i+x])
    print(i, ': ', d[i], '   ', i+x, ': ', d[i+x])

print(d[n])

'''
import sys
input=sys.stdin.readline
n=int(input())
#n일까지 벌 수 있는 최대수익을 저장,
d=[0]*20
tplist=[[0,0]]
for _ in range(n):
  t,p=map(int,input().split())
  tplist.append([t,p])

for i in range(1,n+1):
  x=tplist[i][0]-1
  d[i]=max(d[i-1],d[i])
  d[i+x] = max(d[i-1]+tplist[i][1],d[i+x])
  
print(d[n])
'''
'''
 

Step1)
Output: 최대 수익
N: 남은일자
D[i]: i일 안에 얻을 수 있는 최대 수익

D[1] if i+T[i]-1<=N: D[i] = P[i] => 10
D[2] D[i] = max(P[i-1], P[i]) 
D[3] D[i] = max(D[i-1], )
D[4] D[i] = 

D[i] = D[i+1]
D[i] = Max(D[i+1], D[i+T[i]] + P[i])




EX)
7
3 10
5 20
1 10
1 20
2 15
4 40
2 200
=>45
'''
