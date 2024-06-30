count = int(input())

se = set()

for _ in range(count):
    tmp = input()
    se.add(tmp)


se1 = sorted(se, key = lambda x: (len(x), x) )

for i in se1:
    print(i)