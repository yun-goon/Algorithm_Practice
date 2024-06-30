case = int(input())

num_list = list(map(int, input().split()))
#차이로 오르막이라면
# 높이차이 업데이트

max_uphill = 0

uphill = 0
for i in range(case-1):
    sub = num_list[i] - num_list[i+1]
    if sub < 0: #오르막이라면
        uphill += abs(sub)
        max_uphill = max(uphill, max_uphill)
    else:
        uphill = 0


print(max_uphill)

