'''
센서의 개수 N(1 ≤ N ≤ 10,000), 
둘째 줄에 집중국의 개수 K(1 ≤ K ≤ 1000)

- 집중국의 수신 가능 영역은 고속도로 상에서 연결된 구간으로 나타나게 된다
- 각 집중국의 수신 가능 영역의 길이의 합을 최소화해야 한다

1 3 6 6 7 9
 2 _ 0 1 2
 2 3 0 1 2
 
3 6 7 8 10 12 14 15 18 20 
 _ 1 1 _  _  2  1  _  2
 3 1 1 2  2  2  1  3  2
'''
import sys, heapq
n = int(input())
k = int(input())
sensors = list(map(int,input().split()))

sensors.sort()

distance = []
for i in range(1,n):
    distance.append(sensors[i]-sensors[i-1])
distance.sort()
print(sum(distance[:n-k])) 

