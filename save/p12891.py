# import sys
# input = sys.stdin.readlines
S, P = map(int, input().split())
A = list(input())
checkList = list(map(int, input().split()))


i = 0

countList = [0, 0, 0, 0]  # A C G T
result = 0


def addCountList(index):
    if A[index] == 'A':
        countList[0] += 1
    elif A[index] == 'C':
        countList[1] += 1
    elif A[index] == 'G':
        countList[2] += 1
    elif A[index] == 'T':
        countList[3] += 1


def subtractCountList(index):
    if A[index] == 'A':
        countList[0] -= 1
    elif A[index] == 'C':
        countList[1] -= 1
    elif A[index] == 'G':
        countList[2] -= 1
    elif A[index] == 'T':
        countList[3] -= 1


def validate():
    global result
    count = 0
    if countList[0] >= checkList[0]:
        count += 1
    if countList[1] >= checkList[1]:
        count += 1
    if countList[2] >= checkList[2]:
        count += 1
    if countList[3] >= checkList[3]:
        count += 1
    if count == 4:
        result += 1 


for i in range(P):
    addCountList(i)

validate()

for i in range(S-P):
    subtractCountList(i)
    addCountList(i+P)
    validate()

print(result)

'''
4 2
GATA
1 0 0 1 

9 8
CCTGGATTG
2 0 1 1 
'''
