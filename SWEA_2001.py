T = int(input())

for i in range(1, T+1):
    N, M = map(int, input().split())
    
    board = [list(map(int, input().split())) for _ in range(N)]
    ans = 0

    for r in range(N-M+1):
        for c in range(N-M+1):
            tmp = 0
            for i in range(M):
                for j in range(M):
                    tmp+= board[i][j]

            ans = max(ans, tmp)
    print(f"#{i} {ans}")