import sys
input = sys.stdin.readline

n = int(input())

nums = list(map(int,input().split()))

x = int(input())

start, end = 0, n-1
count = 0

nums.sort()



while start < end:
    tmp = nums[start] + nums[end]

    if tmp == x:
        count += 1
        start +=1
        end -= 1
    elif tmp >x:
        end -= 1
    else:
        start += 1

print(count)
