from collections import deque

T = int(input())

def BFS(r,c):
    global ans
#세팅
    queue = deque([(r,c,0)])

    while queue:

    # 방문
        r,c, cnt = queue.popleft()
        maze[r][c] = 1 # 1로 바꿔서 못가게

    # 탐색
        for d in range(4):
            nr, nc = r+dr[d], c + dc[d]

            if maze[nr][nc] == 3:
                ans = cnt
                return
            
            elif maze[nr][nc] == 0: # 1
                
                queue.append((nr,nc,cnt + 1))


dr = [-1, 1, 0, 0]
dc = [0,0, -1, 1]

for tc in range(1,T+1):
    N = int(input())

    maze = [[1]*(N+2) for _ in range(N+2)] # 패딩
    for i in range(1,N+1):
        maze[i][1:N+1] = map(int,input())

    # print(maze)
    
    # 세팅
    ans = 0
    queue = deque()

    for r in range(1,N+1):
        for c in range(1, N+1):
            if maze[r][c] == 2:
                queue.append((r,c))
                BFS(r,c)

    print(f'#{tc} {ans}')