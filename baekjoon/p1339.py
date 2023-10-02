import sys
input = sys.stdin.readline
n = int(input())
dic ={}
arr=[]
for _ in range(n):
    line = input().rstrip()
    arr.append(line)
    for i in range(len(line)):
        if line[i] not in dic:
            dic[line[i]] = 10**(len(line)-i-1)
        else:
            dic[line[i]] += 10**(len(line)-i-1)

sorted_lst = (sorted(dic.items(), key=lambda item: item[1], reverse = True))
# print(sorted_lst)

num=9
num_dic={}
for item in sorted_lst: 
    num_dic.update({item[0]: num})
    num-=1
# print(num_dic)

ans=0
for item in arr:
    for i in range(len(item)): 
        ans += num_dic.get(item[i])  *10**(len(item)-i-1)
print(ans)
