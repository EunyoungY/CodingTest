import sys
N = int(sys.stdin.readline())
A = [0]*N

for i in range(N):
    A[i] = int(sys.stdin.readline())

result = ""
number = 1
isNo = False
stack = []

for i in range(N):
    while A[i] >= number:
        stack.append(number)
        result += "+"
        number += 1
    if A[i] < number:
        if stack[-1] != A[i]:
            isNo = True
            break
        else:
            stack.pop()
            result += "-"

if isNo == False:
    for i in result:
        print(i)
else:
    print("NO")        

'''
8
4
3
6
8
7
5
2
1

5
1
2
5
3
4
'''
