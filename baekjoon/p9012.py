import sys
input = sys.stdin.readline
t = int(input())

def is_vps(ps):
    result = 'YES'
    stack = []
    for c in ps: 
        if c =='(':
            stack.append('(')
        elif c==')':
            if not stack:
                result = 'NO' 
                print(result) 
                return
            else:
                if stack[-1]=='(':
                    stack.pop()  
    if not stack:  
        result = 'YES'
    else:
        result = 'NO'
                     
    print(result)

for _ in range(t):
    ps = input().rstrip()
    is_vps(ps)
