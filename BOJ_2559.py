# N : 배열의 길이
# K : 간격
N, K = map(int, input().split())

temp_list = list(map(int, input().split()))

temp_sum = sum(temp_list[:K])
T_Max =temp_sum

for start in range(N-K):
    temp_sum -= temp_list[start]
    temp_sum += temp_list[start+K]
    T_Max = max(T_Max, temp_sum)


print(T_Max)
