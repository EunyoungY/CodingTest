import sys
input = sys.stdin.readline
N = int(input())
count = [0]*10001

for i in range(N):
    count[int(input())] += 1

for i in range(10001):
    if count[i] != 0:
        for j in range(count[i]):
            print(i)


# for i in range(10):
#     oneQueue.append
# queue()
# queue()


'''          
4
1
5
3
2
'''
