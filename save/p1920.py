# 1) sorting
# 2) while visiting m, binary search
#   print result

n = int(input())
A = list(map(int, input().split()))
m = int(input())
M = list(map(int, input().split()))
A.sort()


def binary_search(target):
    result = 0
    start = 0
    end = n-1
    while start <= end:
        mid = (start+end)//2
        if A[mid] == target:
            result = 1
            break
        elif A[mid] < target:
            start = mid+1
        else:
            end = mid-1
    print(result)


for i in M:
    binary_search(i)

'''
5
4 1 5 2 3
5
1 3 7 9 5

'''
