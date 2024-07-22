# 투 포인터
N, M = map(int, input().split())

num_list = list(map(int,input().split()))

# print(num_list)
end = 0
count = 0
in_sum = 0
for start in range(N):
    while in_sum < M and end <N:
        in_sum += num_list[end]
        end += 1
    if in_sum == M:
        count += 1
    in_sum -= num_list[start]


print(count)


