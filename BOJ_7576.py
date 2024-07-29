#BFS
import sys
from collections import deque
input = sys.stdin.readline

M, N = map(int, input().split())

box = [list(map(int,input().split())) for _ in range(N)]

dr = [-1, 1, 0,0]
dc = [0, 0, -1, 1]

#익은 토마토 위치를 큐에 넣기 ( 세팅)
queue = deque()
for r in range(N):
    for c in range(M):
        if box[r][c] == 1:
            queue.append((r,c))

# BFS(방문 - 탐색)


while queue:
    # 방문
    r,c = queue.popleft()
    # 탐색
    for d in range(4):
        nr, nc = r+dr[d], c + dc[d]
        if 0 <= nr < N and 0 <= nc < M and box[nr][nc] == 0: # 범위 내에 안익은 녀석이면
            # 방문체크 + 카운팅
            box[nr][nc] = box[r][c] + 1
            queue.append([nr,nc])

# 다 익었는지, 며칠 걸렸는지 
ans = -1
for row in box:
    if 0 in row:
        ans = 0
        break
    else:
        ans = max(max(row), ans)

print(ans - 1)