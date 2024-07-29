import sys
input = sys.stdin.readline
# DFS코드
def DFS(cur, depth, cost):
    global ans
    # 방문
        # 백트래킹 
    if cost >= ans:
        return
        # N개의 도시 다 방문?
    if depth == N:
        # 다방문? 처음으로 돌아가기, return 
        if cost_matrix[cur][0]:
            cost += cost_matrix[cur][0]
            ans = min(cost, ans)
        return

    #탐색
    for nxt in range(N):
        # 0인지 아닌지
        if cost_matrix[cur][nxt] and not visited[nxt]:
            visited[nxt] = 1 # 방문했다
        # 방문체크
        # DFS 재귀
            DFS(nxt, depth+1, cost+ cost_matrix[cur][nxt])
        # 방문 해제
        visited[nxt] =0


N = int(input())
cost_matrix = [list(map(int, input().split()))for _ in range(N)]

# 세팅
ans = float('INF')
visited = [0] * N
DFS(0,1,0)

print(ans)