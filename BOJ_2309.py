key = []
for _ in range(9):
    key.append(int(input()))

total_sum = sum(key)
keep = []

for i in range(9):
    for j in range(i+1, 9):
        if (total_sum - key[i] - key[j] == 100):
            keep = [i, j]
            break
    if keep:
        break

key.pop(max(keep))
key.pop(min(keep))

key.sort()
for height in key:
    print(height)
