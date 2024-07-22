from collections import deque

N, M = map(int, input().split())

adj_matrix = [[0]*(N+1) for _ in range(N+1)]

print(adj_matrix)

for _ in range(M):
    u, v = map(int, input().split())
    adj_matrix[u][v] = 1
    adj_matrix[v][u] = 1

# for i in adj_matrix:
#     print(i)

visited = set([1])
queue = deque([1])

# while queue:
#     cur = queue.popleft()

#     for nxt in range(1, N+1):
#         if not adj_matrix[cur][nxt]:
#             continue
#         if nxt in visited:
#             continue

#         visited.add(nxt)
#         queue.append(nxt)

for nxt in range(1, N+1):
    if 

print(visited)
print(queue)


##############################################

import sys
input = sys.stdin.readline
from collections import deque

def DFS(cur):
    # 방문
    visited1.add(cur)
    # 탐색
    for nxt in adj[cur]:
        if nxt not in visited1:
            DFS(nxt)

def BFS(cur):
    queue = deque([cur])
    visited2.add(cur)

    while queue:
        cur = queue.popleft()

        for nxt in adj[cur]:
            if nxt not in visited2:
                visited2.add(nxt)
                queue.append(nxt)



V, E = map(int, input().split())

# 구조화
    # 빈 판 만들기
adj = [[] for _ in range(V+1)]
    # 간선 정보 입력받기
for _ in range(E):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

visited1 = set() # dfs용


count = 0

# 반복문 돌면서
for i in range(1, V+1):

    # 해당 정점이 방문 안했으면
    if i not in visited1:
    # DFS/BFS 돌고
    # 1 카운팅
        DFS(i)
        count += 1

visited2 = set() # bfs용
# 반복문 돌면서
for i in range(1, V+1):

    # 해당 정점이 방문 안했으면
    if i not in visited2:
    # DFS/BFS 돌고
    # 1 카운팅
        BFS(i)
        count += 1


print(count)