
'''
정점번호, 그 정점까지의 거리

가장 깊은 depth를 찾을 때, 어떤 algorithm을 쓸까? DFS/ BFS? => DFS선택

구상 30분
'''

import sys
n = int(input())
arr = [[] for _ in range(n+1)]

for i in range(n):
    row = list(map(int, input().split()))
    for i in range(1, len(row)-1):
        arr.append([row[0], row[i]])
        arr.append([row[i], row[0]])

print(arr)

'''
입력 16분
1) list에 한 줄을 넣은 후 처리
2) -1나오기 전까지 쌍으로 처리
'''
