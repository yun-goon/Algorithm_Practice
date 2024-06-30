a,b = map(int, input().split())
num_list = []
num_list = list(map(int, input().split()))
max_sum = 0

for i in range(a):
    for j in range(i+1, a):
        for k in range(j+1, a):
            sum = num_list[i] + num_list[j] + num_list[k]
            if sum <= b and sum > max_sum:
                max_sum = sum

print(max_sum)