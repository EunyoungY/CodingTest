import sys

l, c = map(int, sys.stdin.readline().split())
words = sorted(list(map(str, sys.stdin.readline().split())))
answer = []


def back_tracking(depth, start, lst):
    if depth == l:
        vo, co = 0, 0

        for a in lst:
            if a in ['a', 'e', 'i', 'o', 'u']:
                vo += 1
            else:
                co += 1

        if vo >= 1 and co >= 2:
            print(''.join(lst))

        return

    for i in range(start, c):
        back_tracking(depth + 1, i+1, lst+[words[i]])


back_tracking(0, 0, [])
