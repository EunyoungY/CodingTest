n = int(input())

answer = 0
row = [0]*n  # row[1,3,0,2] = 첫번쨰 줄 1번인덱스에 퀸, 2번째줄 3번 인덱스에 퀸
             # (0,1) (1,3) (2,0) (3,2): (x,y) (가로,세로) (행,열)


def is_promising(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x]-row[i]) == abs(x-i): #가로세로 Or 대각선에 있으면
            return False
    return True


def n_queens(x):
    global answer
    if x == n:
        answer += 1
        return
    else:
        for i in range(n): #n=4, x=0이면 (0,0) (0,1) (0,2) (0,3) 을 체크
            row[x] = i  # [x, i]에 퀸 놓기
            if is_promising(x):
                n_queens(x+1)


n_queens(0)
print(answer)
