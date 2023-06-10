'''
구하고자 하는 값: 블루레이 크기 중 최소 = 합의 최소 = start_idx
'''

n, m = map(int, input().split())
A = list(map(int, input().split()))


def binary_search():
    #  start = n  // start =n이 아님, 수가 오름차순으로 정렬되있다는 보장이 없기 때문에 리스트 중 Max값을 찾아야 함
    start = max(A)
    end = sum(A)
    minV = 0  # 블루레이 크기 최소값 비교를 위한 변수
    while start <= end:
        mid = (start+end)//2
        # print(start, mid, end)
        m_count = 1  # 블루레이 개수
        part_sum = 0
        for i in range(n):
            if part_sum+A[i] > mid:
                m_count += 1
                part_sum = 0
            part_sum += A[i]
        # if m_count <= 3: // *실수* 3을 기준으로 함
        if m_count <= m:
            end = mid-1
        elif m_count > m:
            start = mid+1
    print(start)


binary_search()

'''
9 3
1 2 3 4 5 6 7 8 9

9 3
1 9 3 4 5 6 7 8 2

'''
