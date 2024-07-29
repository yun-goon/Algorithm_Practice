import sys
input = sys.stdin.readline

from collections import deque

T = int(input())

for _ in range(T):
    N, K = map(int,input().split())
    build_time = list(map(int, input().split()))

    adj = [[] for _ in range(N+1)]

    in_degree = [0]*(N+1)

    for _ in range(K):
        X, Y = map(int, input().split())
        adj[X].append(Y)

        in_degree[Y] += 1

    goal = int(input())

# 세팅
    queue = deque()
    time_info = [0] * (N+1)

    for i in range(1, N+1):
        if not in_degree[i]:
            queue.append(i)
            time_info[i] = build_time[i]


    # for i in range(1, N+1):
    #     if in_degree[i] == 0:
    #         queue.append(i)

    while queue:
        #방문
        cur = queue.popleft()
        cur_time = time_info[cur]

        if cur == goal:
            ans = cur_time
            break

        # 탐색
        for nxt in adj[cur]:
            in_degree[nxt] -= 1
            time_info[nxt] = time_info[nxt], cur_time + build_time[nxt]

            if not in_degree[nxt]:
                queue.append(nxt)

    print(ans)