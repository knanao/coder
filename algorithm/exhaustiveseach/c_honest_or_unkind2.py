n = int(input())
b = [[] for i in range(n)]
for i in range(n):
    a = int(input())
    for j in range(a):
        x, y = map(int, input().split())
        b[i].append((x-1, y))
ret = 0
# all hypothesis
for s in range(1 << n):
    # hypothesis
    flag1 = True
    cnt = 0
    # one to one
    for i in range(n):
        # check only what you hypothesize to be correct
        if s & (1 << i):
            cnt += 1
            # subject of testimony
            flag2 = True
            for x, y in b[i]:
                # check whether the subject is in the process of being correct
                if ((s >> x) & 1) != y:
                    flag2 = False
                    break
            if not flag2:
                flag1 = False
    if flag1:
        ret = max(ret, cnt)
print(ret)
