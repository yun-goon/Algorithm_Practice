loop = int(input())

work = set()

for _ in range(loop):
    name, state = map(str, input().split())
    if state == 'enter':
        work.add(name)
    elif state == 'leave':
        work.discard(name)

out = sorted(work, reverse= True)

for i in out:
    print(i)