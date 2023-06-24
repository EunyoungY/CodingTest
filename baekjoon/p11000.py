'''
- 정렬해야할 것 같다
    - 앞 순서가 작은 순서대로? 아니면 간격이 작은/큰 순서대로?
- 최소의 강의식을 사용, 모든 수업을 가능하게해야한다.  

- [[(1 3),(3,5)] [2 4]] or arr
- O(n) 이하의 알고리즘
- #pop/push

1 9 
2 3 
3 4 
'''
import heapq
import sys
input = sys.stdin.readline
n = int(input())
arr=[]
for i in range(n):
    start, end = map(int, input().split())
    arr.append((start, end))

arr.sort()

room =[]
heapq.heappush(room, arr[0][1])
 
for i in range(1, n):
    if arr[i][0] < room[0]:
        heapq.heappush(room, arr[i][1])
    else:
        heapq.heappop(room)
        heapq.heappush(room, arr[i][1])
print(len(room))
'''
1) 시작시간을 기준으로 정렬
2) 첫 회의의 종료 시간을 큐에 넣기 room: [3  ]
3) n-1번 반복(두번째 회의부터 첫번째 회의와 비교)
    if 두번째 회의 시작시간(2) < 첫번쨰 회의 끝나는 시간(3)
        room에 두번째 회의 끝나는 시간 넣기
    else
        (종료시간이 빠른 회의실부터 뽑아서 다음 회의를 이어 개최할 수 있게 해야하므로)
        room에서 종료시간이 가장 빠른 원소 Pop
        현재 회의의 종료 시간 push
'''