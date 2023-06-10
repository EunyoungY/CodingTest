import sys
input = sys.stdin.readline
N, K = map(int, input().split())
A = list(map(int, input().split()))


def quickSort(start, end, K):
    global A
    if start < end:
        pivot = partition(start, end)
        if pivot == K:
            return
        elif K < pivot:
            quickSort(start, pivot-1, K)
        else:
            quickSort(pivot+1, end, K)


def swap(i, j):
    global A
    temp = A[i]
    A[i] = A[j]
    A[j] = temp


def partition(start, end):
    global A

    if start+1 == end:  # 데이터가 2개인 경우 바로 비교하여 정렬
        if A[start] > A[end]:
            swap(start, end)
        return end

    middle = (start+end)//2
    swap(start, middle)
    pivot = A[start]
    i = start+1
    j = end

    while i <= j:
        while pivot < A[j] and j > 0:
            j = j-1
        while pivot > A[i] and i < len(A)-1:
            i = i+1
        if i <= j:
            swap(i, j)
            i = i+1
            j = j+1

    A[start] = A[j]
    A[j] = pivot
    return j


quickSort(0, N-1, K - 1)
print(A[K-1])

'''
5 2
4 1 2 3 5
'''
