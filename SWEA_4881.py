T = int(input())

def DFS(depth, cnt): # 층, 더해줄 숫자
    global ans
    if depth == N: # 모든 행을 거쳐서 내려왔다
        ans = min(ans, cnt) # 정답과 cnt 값이랑 비교
        return
    
    if cnt >= ans: # 백트래킹, 작은거 찾아야해서 크면, 그냥 리턴해버림
        return



    for idx in range(N):
        if not visited[idx]: #안뽑혔으면
            # cnt += matrix[depth][idx] # 더해줘야함
            visited[idx] = 1 # 이번 열 방문 표시
            DFS(depth+1, cnt+matrix[depth][idx]) # 다음 depth cnt 가 더해진, 돌아올때는 안더해진상태야
            visited[idx] = 0
            # cnt -= matrix[depth][idx] # 더해서 넘기면 빼줘야함.


for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    ans = float("INF")
    visited = [0] * N

    DFS(0,0)
    print(f'#{tc} {ans}')

