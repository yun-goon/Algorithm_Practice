import sys
input = sys.stdin.readline


dr = [-1, 1, 0,0]
dc = [0, 0, -1, 1]


def DFS(r,c):
    tmp_o, tmp_v = 0, 0

    if field[r][c] == 'o':
        tmp_o += 1
    elif field[r][c] == 'v':
        tmp_v += 1

    field[r][c] = '#'




    while stack:  
        #방문
        r,c = stack.pop()
    #탐색
        for d in range(4):
            nr, nc = r+dr[d], c+dc[d]
            if 0 > nr or nr >= R or 0 > nc or nc >= C or field[nr][nc] == '#':
                continue

            if field[nr][nc] == 'o':
                tmp_o += 1
            elif field[nr][nc] == 'v':
                tmp_v += 1

            field[nr][nc] = '#'


            stack.append((nr,nc))

    # 후처리
    if tmp_o > tmp_v:
        tmp_v = 0
    else:
        tmp_v = 0
    return tmp_o, tmp_v

R, C = map(int, input().split())

# field = [['#']*(C+2) for _ in range(R+2)]
# for i in range(1, R+1):
#     field[1:C+1] = list(input().rstrip())

field = [list(input().rstrip() for _ in range(R))]
# print(field)





o = v = 0 # 양, 늑대의 갯수 

for r in range(R):
    for c in range(C):
        if field[r][c] != '#': #울타리가 아니라면
            stack = [(r,c)]
            tmp_o, tmp_v = DFS(r,c)
            o += tmp_o
            v += tmp_v

print(o,v)