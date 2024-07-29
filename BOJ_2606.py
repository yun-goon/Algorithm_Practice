import sys
input = sys.stdin.readline

def dfs(now):
    if now not in visited:
        visited.add(now)

    for after in range(N + 1):
        if adj[now][after] and after not in visited:
            dfs(after)

N = int(input())
E = int(input())

adj = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(E):
    start, end = map(int, input().split())
    adj[start][end] = 1
    adj[end][start] = 1

visited = set()

dfs(1)

print(len(visited) - 1)

# # 세팅

# '''
# 1. 방문 기록지
# 2. 방문 예정지
# 3. 출발지
# '''
# # 1. 방문 기록지
# visited1 = set() # 방법 1, in 으로 확인 
# visited2 = [0]*(V+1) # 방법2, 리스트, 방문했으면 1로 변환, 인덱스로 확인

# # 2. 방문 예정지, [출발지]
# stack = deque([1])




# #방문 예정지가 빌 때 까지
# while stack:

#     # 방문
#     cur = stack.pop()
#     visited1.add(cur)

#     visited2[cur] = 1

#     # 탐색
#     for nxt in adj_matrix[cur]:
#         if nxt !=0:
#             continue
#         if nxt in visited1:
#             continue
#         if visited2[nxt]:
#             continue

import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
E = int(input())

adj = [[] for _ in range(N+1)]
for _ in range(E):
    start, end = map(int, input().split())
    adj[start].append(end)
    adj[end].append(start)

queue = deque([1])
visited = set([1])

while queue:
    cnt = queue.popleft()

    for nxt in adj[cnt]:
        if nxt not in visited:
            visited.add(nxt)
            queue.append(nxt)

print(len(visited)-1)