import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())

queue = deque([N])
visited = [0] * 100001
visited[N] = 1  # 시작점 방문 체크 및 시작 시간

while queue:
    current = queue.popleft()

    if current == K:
        print(visited[current] - 1)  # 도착점에서의 시간 출력 후 종료
        break

    for next_pos in (current - 1, current + 1, current * 2):
        if 0 <= next_pos <= 100000 and not visited[next_pos]:
            visited[next_pos] = visited[current] + 1
            queue.append(next_pos)
