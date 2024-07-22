import sys
input = sys.stdin.readline

from collections import deque

N, K = map(int, input().split())

#세팅
queue = deque([N])
visited = [0] * 100001
visited[N] = 1 # 방문 체크

while queue:
    # 방문
    cur = queue.popleft()

    if cur == K:
        break

    # 탐색
    for nxt in (cur+1, cur-1, cur*2):
        if 0<= nxt < 100000 and not visited[nxt]: # 범위 내에 방문 안했으면
            visited[nxt] = visited[cur] + 1
            queue.append(nxt)

print(visited[K] -1 )
