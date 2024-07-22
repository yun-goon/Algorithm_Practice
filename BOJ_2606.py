from collections import deque

V = int(input())
E = int(input())
adj_lst = [[] for _ in range(V+1)]

for _ in range(E):
    s,e = map(int, input().split())
    adj_lst[s][e] = 1 # 가중치 줄땐 w
    adj_lst[e][s] = 1 # 가중치 줄땐 w


visited = set()

def DFS(cur):
    visited.add(cur)

    for nxt in adj_lst[cur]:
        if nxt not in visited:
            DFS(nxt)

DFS(1)
print(len(visited)- 1)

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

