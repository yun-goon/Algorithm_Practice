from collections import deque


dr = [-1, 1, 0,0]
dc = [0,0, -1, 1]
'''
아무 양배추 꺼내기
돌리면서 인접 애들 모두 꺼내오기

'''
for _ in range(int(input())):
    M, N, K = map(int, input().split())

    cabages = set()

    for _ in range(K):
        c,r = map(int, input().split())
        cabages.add((r,c))

    ans = 0

    while cabages:
        r,c = cabages.pop() # 집합이라 랜덤으로 튀어 나옴

        queue = deque([(r,c)])

        while queue:
            #방문
            r, c = queue.popleft()

            # 탐색
            for d in range(4):
                nr, nc = r+dr[4], c+ dc[4]
                if (nr, nc) in cabages:
                    queue.append((nr,nc))
                    cabages.discard((nr,nc))
        ans += 1

