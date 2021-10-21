n, m = list(map(int, input().split()))
s = []
for _ in range(m):
    i = list(map(int, input().split()))
    s += [i[1:]]
p = list(map(int, input().split()))

ret = 0
for i in range(1 << n):
    for j in range(m):
        count = 0
        for k in s[j]:
            if i & (1 << (k-1)):
                count += 1
        if count % 2 != p[j]:
            break
    else: 
        ret += 1
print(ret)
