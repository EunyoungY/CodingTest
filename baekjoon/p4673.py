'''
time: 1 sec => 2천만번 이내

- 33은 39의 생성자
- 생성자가 없는 숫자를 셀프 넘버

input: x
output: 10000보다 작거나 같은 셀프 넘버를 한 줄에 하나씩 출력
'''
n=10000
arr=[]
for i in range(n+1):
    arr.append(i) 
 
for i in range(n+1):
    val = i
    for j in str(i):
        val += int(j) 
    if val in arr:
        arr.remove(val)
        
for i in arr:
    print(i)

# for i in arr:
#     if arr[i] == 0:
#         print(i)