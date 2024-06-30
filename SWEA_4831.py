def minimum_charges(K, N, M, stations):
    current = 0
    charges = 0
    stations.append(N)  # 종점에도 충전기가 있는 것처럼 처리
    
    while current < N:
        # 현재 위치에서 갈 수 있는 가장 먼 충전기를 찾는다
        best_next = -1
        for station in stations:
            if station > current + K:
                break
            if station > current:
                best_next = station
        
        if best_next == -1:
            # 더 이상 갈 수 있는 충전기가 없으므로 도달 불가능
            return 0
        
        # 충전기까지 이동
        current = best_next
        charges += 1

    return charges - 1  # 처음 출발지의 충전은 카운트하지 않으므로 -1

T = int(input())
results = []

for case_number in range(1, T+1):
    K, N, M = map(int, input().split())
    stations = list(map(int, input().split()))
    
    result = minimum_charges(K, N, M, stations)
    results.append(f"#{case_number} {result}")

for result in results:
    print(result)
