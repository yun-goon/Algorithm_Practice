
N = int(input())
check = [0] * N
check_right = [0]*(2*N -1)
check_left = [0]*(2*N -1)

ans = 0


def N_Queen(depth):
    global ans
    # 방문
    if depth == N:
        ans += 1
        return
    

    #탐색
    for idx in range(N):
        if check[idx] or check_right[depth - idx] or check_left[depth + idx]:
            continue
        check[idx] = 1
        check_right[depth - idx] = 1
        check_left[depth + idx] = 1

        N_Queen(depth+1)

        check[idx] = 0
        check_right[depth - idx] = 0
        check_left[depth + idx] = 0

N_Queen(0)
print(ans)