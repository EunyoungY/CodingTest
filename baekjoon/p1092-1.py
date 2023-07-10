from collections import deque
n = int(input())
cranes = list(map(int, input().split()))
m = int(input())
boxes = list(map(int, input().split()))

cranes.sort(reverse=True)
boxes.sort(reverse=True)

answer = 0
if boxes[0] > cranes[0]:
    print(-1)
else:
    while boxes:
        for crane in cranes:
            for box in boxes:
                if crane >= box:
                    boxes.remove(box)
                    break
        answer += 1
    print(answer)
