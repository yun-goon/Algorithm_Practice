import sys
input = sys.stdin.readline

N = int(input())

times = []

for _ in range(N):
    s, e = map(int, input().split())
    times.append((s,e))

times.sort()
times.sort(key=lambda x : x[1])

stand = -1
out = 0
for s,e in times:
    if s >= stand:
        out += 1
        stand = e

print(out)