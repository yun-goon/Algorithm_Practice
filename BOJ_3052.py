num_list = []

for _ in range(10):
    num_list.append(int(input())%42)



num_list = list(set(num_list))

print(len(num_list))