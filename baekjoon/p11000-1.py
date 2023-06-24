import heapq, sys
input = sys.stdin.readline
n = int(input())

lessons = []
for i in range(n):
    start, end = map(int, input().split())
    lessons.append((start, end))

lessons.sort() 

room =[lessons[0][1]]
for i in range(1, n):
    start, end = lessons[i][0],  lessons[i][1]
    if start<room[0]:
        heapq.heappush(room, end)
    else:
        heapq.heappop(room)
        heapq.heappush(room, end)

print(len(room))
