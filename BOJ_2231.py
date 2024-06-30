s1 = input()

# num = int(s1)
# part = 0
# for i in s1:
#     part += int(i)

# out = num + part
# print(out)

n = 0

sum = 0
flag = 1
for l in range(int(s1)):
    sum = l
    for i in str(l):
        sum += int(i)
    
    if s1 == str(sum):
        print(l)
        flag = 0
        break
if flag:
    print(0)