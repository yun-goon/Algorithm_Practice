'''
5 3
5 4 3 2 1
1 3
2 4
5 5

첫째 줄에 수의 개수 N과 합을 구해야 하는 횟수 M이 주어진다. 
둘째 줄에는 N개의 수가 주어진다. 
수는 1,000보다 작거나 같은 자연수이다.
셋째 줄부터 M개의 줄에는 합을 구해야 하는 구간 i와 j가 주어진다.

'''

N, M = map(int, input().split())
num_list = list(map(int, input().split()))

for _ in range(M):
    n_sum = 0
    i, j = map(int, input().split())
    tmp = num_list[i-1:j]   
    n_sum = sum(tmp)
    print(n_sum)

# 위는 O(N*M)의 시간복잡도

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))

for i in range(1, len(nums)):  # 누적합
    nums[i] += nums[i-1]

for _ in range(M):
    s, e = map(int, input().split())
    subtract = 0 if s == 1 else nums[s-2]
    print(nums[e-1] - subtract)

#이건 누적합을 이용, O(N+M)의 시간복잡도
