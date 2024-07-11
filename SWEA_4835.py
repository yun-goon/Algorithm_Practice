T = int(input())

for test_case in range(1, T+1):
    sum_list = []
    N, M = map(int, input().split())
    num_list = list(map(int, input().split()))
    for i in range(0,N-M+1):
        tmp = num_list[i:i+M]
        sum_list.append(sum(tmp))

    print(f'#{test_case} {max(sum_list) - min(sum_list)}')