
'''
- 1분에 박스를 하나씩 배에 실을 수 있다 ** 얘 때문에 시간 걸림
- N은 50보다 작거나 같은 자연수
- 박스의 수 M은 10,000보다 작거나 같은 자연수
output: 첫째 줄에 모든 박스를 배로 옮기는데 드는 시간의 최솟값

- 오답 이유: 만약 모든 박스를 배로 옮길 수 없으면 -1을 출력한다.
'''

import sys 
input = sys.stdin.readline

n = int(input())  # num of cranes
cranes = list(map(int, input().split()))
m = int(input())  # num of boxes
boxes = list(map(int, input().split()))

cranes.sort(reverse=True)
boxes.sort(reverse=True)
 
mins = 0
if cranes[0] < boxes[0]:
    print(-1)
    sys.exit() #

 
# while boxes:
#     for crane in cranes:
#         if not boxes:
#             break
#         elif crane < boxes[-1]:
#             break
#         for box in boxes:
#             if crane >= box:
#                 boxes.remove(box)
#                 break
#     mins += 1
# print(mins)

'''
3
2 3 8
3
2 5 7
'''
    
i = 0
mins = 0
if cranes[0] < boxes[0]:
    print(-1)
    sys.exit()

while boxes:
    if i % n == 0:
        mins += 1
    # if cranes[i] >= boxes[i]:
    if cranes[i % n] >= boxes[0]:
        boxes.pop(0) # //TODO
    i += 1
print(mins)

'''
2 
'''