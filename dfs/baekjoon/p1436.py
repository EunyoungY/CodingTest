'''
Plan 23mins
1<=n<=10000
종말의 수란 어떤 수에 6이 적어도 3개 이상 연속으로 들어가는 수
666-1666-2666-6666 ...9666 - 6666

666
1666
2666
3666
4666
5666
6660~6669
7666
8666
9666

0666~5666  #6개
6660~6669  #10개
7666~9666  #3개

10666~15666  
16660~16669 
17666~19666

20666~25666
26660~26669
27666~29666

number = 666
n #
count = 0

while count < n
for 0-6
    cnt+=1
    num+=1000
num-=6
for 0-10
    cnt+=1

'''
#implement: 23mins+51
#1차접근: while문 안 for문으로 숫자를 더하는 방식으로 접근 => 코드 너무 더럽고 복잡해짐
#2차 접근: string으로
#3차
# 처음 문제 보고, 
import sys
n = int(input())
num = 666
cnt = 1
while cnt <n:
    num+=1
    if '666' in str(num):
        cnt+=1
print(num)

# while cnt < n:
#     cnt+=1
#     if str(num)[-4:] == '5666':
#         num+=994
#     elif str(num)[-4:] == '6669':
#         num+=997
#     elif 6660<=int(str(num)[-4:])<=6669: 
#         num+=1
#     else: num+=1000
#     print(cnt, num)
    
        

# Learned
#####끝에서 n개 문자 추출 myString[-4:]
#if '666' in str(test):