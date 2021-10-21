import itertools

n, m = map(int, input().split())
g = [[] for i in range(n)]
for i in range(n):
    a, b = map(lambda x: int(x)-1, input().split())
    g[a].append(b)
    g[b].append(a)

ret = 0
if n == 2:
    if 1 in g[0]:
        print(1)
    else:
        print(0)
    exit()
for p in itertools.permutations(range(1, n)):
    if p[0] in g[0]:
        flag = True
        for i in range(n-2):
            if p[i+1] not in g[p[i]]:
                flag = False
                break
        if flag:
            ret += 1
print(ret)
