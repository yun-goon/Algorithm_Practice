import sys

input = sys.stdin.readline


K = int(input())


nums = []
for _ in range(K):
    tmp = int(input())
    if tmp == 0:
        nums.pop()
    else:
        nums.append(tmp)

print(sum(nums))