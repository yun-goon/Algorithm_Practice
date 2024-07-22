# DFS

import sys
input = sys.stdin.readline


dr = [-1, 1, 0,0]
dc = [0, 0, -1, 1]

#DFS
def DFS(r,c, num):
    #방문
    if len(num) == 6:
        cases.add(num)
        return

    #탐색
    for d in range(4):
        nr, nc = r+dr[d], c + dc[d]
        if 0 <= nr < 5 and 0 <= nc < 5:
            DFS(nr,nc,num+board[nr][nc])        




board = [input().rstrip().split() for _ in range(5)]
# print(board)

cases = set()
ans = 0

for r in range(5):
    for c in range(5):
        DFS(r,c,board[r][c])


print(len(cases))