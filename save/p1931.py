from queue import PriorityQueue
n = int(input())
que = PriorityQueue()

for _ in range(n):
    a, b = map(int, input().split())
    que.put([b, a])

count = 0
end = 0
for i in range(n):
    pair = que.get()
    if pair[1] >= end:
        end = pair[0]
        count += 1 
print(count)


'''
2
0 2
1 1

11
1 4   
3 5   
0 6   
5 7   
3 8   
5 9   
6 10  
8 11  
8 12   
2 13  
12 14  
'''
