from collections import deque
v = int(input())
A = [[] for i in range(v+1)]
visited = [False] * (v+1)
distance = [0] * (v+1)
for i in range(1, v+1):
    numbers = list(map(int, input().split()))
    j = 1
    while True:
        if numbers[j] == -1:
            break
        A[i].append((numbers[j], numbers[j+1]))
        j += 2


def BFS():
    global distance
    queue = deque()
    max_dist = 0
    for i in range(1, v+1):
        distance = [0] * (v+1)
        queue.append((i, 0))
        visited[i] = True
        while queue:
            now_node = queue.popleft()  # now_node = (1,0)
            for j in A[i]:
                if not visited[j[0]]:
                    queue.append(j)  # j=(1,2)
                    visited[j[0]] = True
                    distance[j[0]] = now_node[1] + j[1]
        if max_dist < max(distance):
            max_dist = max(distance)
    print(max_dist)


BFS()


'''
5
1 3 2 -1
2 4 4 -1
3 1 2 4 3 -1
4 2 4 3 3 5 6 -1
5 4 6 -1
'''
