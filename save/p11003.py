L, N = map(int, input().split())
A = list(map(int, input().split()))
minTest = []
D = ""
for i in range(L):
    if i <= N-1:
        minTest.append(min(A[i], A[i+1]))
    else:
        minTest.pop(0)
        minTest.append(min(A[i], A[i+1]))

    D += str(min(minTest))+' '


print(D)
'''
12 3
1 5 2 3 6 2 3 7 3 5 2 6


계속 min값을 구하게 되면 O(NlogN)의 시간복잡도. 
일반적인 list에서는 pop연산이 느리다.
=> deque와 sliding window를 활용하여 문제를 해결
'''
