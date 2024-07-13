# 1. 빈 판 N*N
'''
시작지점은 0,0
우, 하 ,좌, 상 순서대로 감.
dr = []
dc = []

반복문을 돌면서
for num in range(1, N^2 +1)
matrix [r][c] == num
nr, nc = r + dr[d], c + dc[d]
if 범위가 벗어나면?
d += 1
d = (d+1)%4
nr,nc 다시 구하기

검토 o -> 갱신
검토 x -> 방향전환 -> 갱신
'''

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    matrix = [[0]*(N+2) for _ in range(N+2)] #빈 matrix 설정
    # print(board)
    num = 1
    r,c = 1,1
    d = 0

    dr = [0,1,0,-1]
    dc = [1,0,-1,0]

    for i in range(N+2):
        matrix[0][i] = -1
        matrix[N+1][i] = -1
        matrix[i][0] = -1
        matrix[i][N+1] = -1

    for num in range(1, N**2+1):
        matrix[r][c] = num # 숫자 넣고
        # print("num", num)
        if matrix[r + dr[d]][c + dc[d]] != 0: #범위 체크 하고
            d = (d+1) % 4 #방향 바꾸고
        # print("d", d)

        r = r + dr[d]
        c = c + dc[d]

        # print(r,c)
    
    snail = []
    for l in matrix[1:N+1]:
        snail.append(l[1:N+1])

    print(f'#{tc}')
    for line in snail:
        print(*line)





# T = int(input())
# # 델타 탐색 세팅


# dr = [0,1,0,-1]
# dc = [1,0,-1,0]

# for tc in range(1, T+1):
#     N = int(input())

# # 빈 판 만들기
#     snail = [[0]*N for _ in range(N)]


# # 초기 세팅(좌표, 방향)
#     r,c,d = 0,0,0

# #반복문
#     for num in range(1, N**2+1):
#         # 숫자 넣기
#         snail[r][c] = num

#         # 다음 좌표 찍어보기
#         nr, nc = r + dr[d], c + dc[d]
#         # 해당 좌표가 유망한 곳인지 검토
#         if nr < 0 or nr >= N or nc < 0 or nc >= N or snail[nr][nc] != 0: #벗어났거나 이미 방문했으면,
#             #방향 전환하고 새로운 좌표 찍기
#             d = (d+1)%4
#             nr, nc = r + dr[d], c + dc[d]
#         # 갱신
#         r,c = nr, nc

#     print(f'#{tc}')
#     for line in snail:
#         print(*line)