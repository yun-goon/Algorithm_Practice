import sys
input = sys.stdin.readline

case = int(input())

points = []

for _ in range(case):
    x,y = map(int, input().split())
    points.append((x,y))

points.sort()

for i in points:
    print(*i)