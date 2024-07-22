N = int(input())

info = []

for _ in range(N):
    w, h = map(int,input().split())
    info.append((w,h))
ranks = []
for i in range(N):
    rank = 1
    for j in range(N):
        if i != j:
            if info[i][0] < info[j][0] and info[i][1] < info[j][1]:
                rank += 1
    ranks.append(rank)

print(' '.join(map(str, ranks)))