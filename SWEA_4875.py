'''
T = int(input())

def DFS(r, c):
    global cnt
    arr[r][c] = 0
    cnt += 1

    for d in range(4):
        nr, nc = r+dr[d], c + dc[d]
        if 0 <= nr < 5 and 0 < nc < 5 and arr[nr][nc] == 0:
            DFS(nr,nc)

def find_point(num):


for tc in range(1,T+1):
    N = int(input())
    mirro = []
    for i in range(N):
        tmp = input()
        mirro.append(tmp)
    
    ans = 0
    cnt = 0

    dr = [-1, 1, 0, 0]
    dc = [0,0, -1, 1]


    

    print(mirro)



'''



def DFS(r,c):
    global ans
    # 방문
    visited.add((r,c))

    # 탐색
    for d in range(4):
        nr, nc = r+dr[d], c + dc[d]
        if 0 > nr or nr >= N or 0 > nr or nc >= N:
            continue

        if maze[nr][nc] == 3:
            ans = 1
            return
        
        elif maze[nr][nc] == 0 and (nr, nc) not in visited:
            DFS(nr,nc)



dr = [-1, 1, 0, 0]
dc = [0,0, -1, 1]

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    maze = [list(map(int,input()) for _ in range(N))]

    # 세팅
    ans = 0
    visited = set()
    for r in range(N):
        for c in range(N):
            if maze[r][c] == 2:
                DFS(r,c)

    print(f'{tc} {ans}')




#################### 
#1. 방문지 표시
# 2. 패딩

def DFS(r,c):
    global ans
    # 방문
    visited.add((r,c))

    maze[r][c] = 1 # 1로 바꿔서 못가게

    # 탐색
    for d in range(4):
        nr, nc = r+dr[d], c + dc[d]

        if maze[nr][nc] == 3:
            ans = 1
            return
        
        elif maze[nr][nc] == 0: # 1
            DFS(nr,nc)



dr = [-1, 1, 0, 0]
dc = [0,0, -1, 1]

T = int(input())

for tc in range(1,T+1):
    N = int(input())

    maze = [[1]*(N+2) for _ in range(N+2)] # 패딩
    for i in range(1,N+1):
        maze[i][1:N+1] = map(int,input())

    # print(maze)
    
    # 세팅
    ans = 0
    visited = set()
    for r in range(1,N+1):
        for c in range(1, N+1):
            if maze[r][c] == 2:
                DFS(r,c)

    print(f'{tc} {ans}')