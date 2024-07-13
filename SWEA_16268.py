# T = int(input())

# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     # board = [[0]*M for _ in range(N)]

#     r,c = 0,0
#     dr = [-1, 1, 0, 0]
#     dc = [0, 0, -1, 1]

#     board = []
#     for _ in range(N):
#         board.append(list(map(int, input().split())))



#     print(board)

T = int(input())

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for tc in range(1, T+1):
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    # 패딩 사용
    # board = [[0]*(M+2) for _ in range(N+2)]
    # for i in range(1, N+1):
    #     board[1:1+M] = list(map(int, input().split()))

    ans = 0

    for r in range(N): # 순회
        for c in range(M):
            cnt = board[r][c]
            #델타 탐색
            for d in range(4):
                nr, nc = r + dr[d], c + dc[d]
                if 0 <= nr < N and 0 <= nc <M:
                    cnt += board[nr][nc]
            ans = max(ans, cnt)

    print(f'#{tc} {ans}')





T = int(input())

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for tc in range(1, T+1):
    N, M = map(int, input().split())
    # board = [list(map(int, input().split())) for _ in range(N)]

    # 패딩 사용
    board = [[0]*(M+2) for _ in range(N+2)]
    for i in range(1, N+1):
        board[i][1:1+M] = list(map(int, input().split()))

    ans = 0

    for r in range(1, N+1): # 순회
        for c in range(1, M+1):
            cnt = board[r][c]
            #델타 탐색
            for d in range(4):
                nr, nc = r + dr[d], c + dc[d]
                cnt += board[nr][nc]
            ans = max(ans, cnt)

    print(f'#{tc} {ans}')
