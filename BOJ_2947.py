num_list = list(map(int, input().split()))

for i in range(5):
    for j in range(4):
        if num_list[j] > num_list[j+1]:
            tmp = num_list[j]
            num_list[j] = num_list[j+1]
            num_list[j+1] = tmp
            print(" ".join(map(str,num_list)))
