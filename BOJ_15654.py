import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr = sorted(list(map(int,input().split()))) # 사전 증가순으로 출력 조건

ans = [0]*M
visited = [0]*N

def perm(depth):
    if depth == M:
        print(*ans)
        return
    
    for i in range(N):
        if not visited[i]:
            ans[depth] = arr[i]

            visited[i] = 1
            perm(depth+ 1)
            visited[i] =0

perm(0)
