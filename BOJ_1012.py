# T = int(input())

# def DFS(r,c):
#     maps[r][c] = 0

#     for d in range(4):
#         nr, nc = r+dr[d], c + dc[d]
#         if 0 > nr or nr > M or 0 > nc or nc > M:
#             continue
#         elif maps[nr][nc] == 1:
#             DFS(nr, nc)



# dr = [-1, 1, 0,0]
# dc = [0,0, -1, 1]

# for tc in range(T):
#     M, N, K = map(int, input().split())

#     maps = [[0]* M for _ in range(N)]

#     ans = 0

#     for _ in range(K):
#         x, y = map(int, input().split())
#         maps[y][x] = 1


#     for r in range(M):
#         for c in range(N):
#             DFS(r,c)
#             ans += 1
    
#     print(ans)



import sys
input = sys.stdin.readline
from collections import deque

def BFS(r,c):
    #세팅
    queue = deque([(r,c)])

    while queue:

        #방문
        r,c = queue.popleft()
        field[r][c] =0

        #탐색
        for d in range(4):
            nr, nc = r+dr[d], c + dc[d]
            if 0 <= nr < N and 0<= nc < M and field[nr][nc] == 1:
                queue.append((nr,nc))

def DFS(r,c):
    #방문
    field[r][c] = 0
    # 탐색
    for d in range(4):
        nr, nc = r+dr[d], c + dc[d]
        if 0 <= nr < N and 0<= nc < M and field[nr][nc] == 1:
            DFS(nr, nc)


dr = [-1, 1, 0,0]
dc = [0,0, -1, 1]
for _ in range(int(input())):
    M, N, K = map(int, input().split())
    #구조화
    field = [[0]*M for _ in range(N)]
    for _ in range(K):
        c, r = map(int, input().split())
        field[r][c] = 1
    # 반복문 돌며, 인접한 1의 갯수 세주기
    cnt =0
    for r in range(N):
        for c in range(M):
            if field[r][c] ==1:
                DFS(r,c)
                cnt += 1
    
    print(cnt)

'''


import sys
input = sys.stdin.readline
from collections import deque

def BFS(r,c):

def DFS(r,c):


for _ in range(int(input())):
    M, N, K = map(int, input().split())
    #구조화
    field = [[0]*M for _ in range(N)]
    for _ in range(K):
        c, r = map(int, input().split())
        field[r][c] = 1
    # 반복문 돌며, 인접한 1의 갯수 세주기
    for r in range(N):
        for c in range(M):
            if field[r][c] ==1:
                DFS(r,c)
                cnt += 1
    
'''