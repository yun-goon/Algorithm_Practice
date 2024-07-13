def solve(N, M, board):
    start_with_B = [('B' if (i+j) % 2 == 0 else 'W') for i in range(8) for j in range(8)]
    start_with_W = [('W' if (i+j) % 2 == 0 else 'B') for i in range(8) for j in range(8)]
    
    min_changes = float('inf')
    
    for i in range(N - 7):
        for j in range(M - 7):
            current_B = 0
            current_W = 0
            for x in range(8):
                for y in range(8):
                    if board[i+x][j+y] != start_with_B[x*8+y]:
                        current_B += 1
                    if board[i+x][j+y] != start_with_W[x*8+y]:
                        current_W += 1
            min_changes = min(min_changes, current_B, current_W)
    
    return min_changes

N, M = map(int, input().split())
board = [input() for _ in range(N)]

print(solve(N, M, board))
