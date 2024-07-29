from collections import deque

def solution(n, wires):
    answer = 101

    # 구조화

    adj = [[] for _ in range(n+1)]
    in_degree = [0] * (n+1)

    for s,e in wires:
        adj[s].append(e)
        adj[e].append(s)
        in_degree[s] += 1
        in_degree[e] += 1
    
    # 세팅
    queue = deque([node for node in range(1, n+1) if in_degree[node] == 1])
    rank = [1] * (n+1)


    # 방문
    while queue:
        cur = queue.popleft()
        answer = min(answer, abs(rank[cur]*2 - n))

    # 탐색
        for nxt in adj[cur]:
            in_degree[nxt] -= 1
            rank[nxt] += rank[cur]

            if in_degree[nxt] == 1:
                queue.append(nxt)

    return answer


