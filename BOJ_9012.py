import sys
input = sys.stdin.readline

T = int(input())


for tc in range(T):
    cases = []
    lst = input().rstrip()
    for i in lst:
        if i == ')':
            cases.pop()
        elif i == '(':
            cases.append(i)

        else:
            cases= True
            break
            
    if cases:
        print("YES")

    else:
        print("NO")
