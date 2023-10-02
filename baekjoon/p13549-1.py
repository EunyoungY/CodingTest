from collections import deque
import sys
n, k = map(int, input().split())

q = deque()
time = [sys.maxsize]*100001
q.append(n)
time[n] = 0
while q:
    now = q.popleft()
    if now == k:
        print(time[k])
        break
    if 0 <= now*2 <= 100000 and time[now*2] > time[now]:
        time[now*2] = time[now]
        q.appendleft(now*2)
    if 0 <= now+1 <= 100000 and time[now+1] > time[now]+1:
        time[now+1] = time[now]+1
        q.append(now+1)
    if 0 <= now-1 <= 100000 and time[now-1] > time[now]+1:
        time[now-1] = time[now]+1
        q.append(now-1)

'''
time table을 만들어야 하는 이유: 처음 찾은 경로가 최단거리가 아닐 수 있음
'''

# from collections import deque
# n, k = map(int, input().split())

# q = deque()
# time = [-1]*100001
# q.append(n)
# time[n] = 0
# while q:
#     now = q.popleft()
#     if now == k:
#         print(time[k])
#         break
#     if 0 <= now*2 <= 100000 and time[now*2] == -1:
#         time[now*2] = time[now]
#         q.appendleft(now*2)
#     if 0 <= now+1 <= 100000 and time[now+1] == -1:
#         time[now+1] = time[now]+1
#         q.append(now+1)
#     if 0 <= now-1 <= 100000 and time[now-1] == -1:
#         time[now-1] = time[now]+1
#         q.append(now-1)
