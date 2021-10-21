n = int(input())
ret = 0

for i in range(1, n+1):
    count = 0
    for j in range(i+1):
        if j % 2 == 0:
            continue
        if i % j == 0:
            count += 1
    if count == 8:
        ret += 1
print(ret)
