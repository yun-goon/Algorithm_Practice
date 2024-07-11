import sys
input = sys.stdin.readline

def binary_search(l,r):
    c = (l+r)//2

    if l > r : #새로운 종료조건 - 끝까지 못찾았다면
        return c # 최적값
    budget = 0

    for req in reqs:
        budget += min(req,c)
    

    if budget == m:
        return c
    elif budget > m:
        return binary_search(l, c-1)
    elif budget < m:
        return binary_search(c+1, r)
    

n = int(input())
reqs = list(map(int, input().split()))
m = int(input())

print(binary_search(0, max(reqs)))


