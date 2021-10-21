n = int(input())
s = list(map(int, input().split()))
t = list(map(int, input().split()))

for i in range(n*2):
    # t[2] = min(t[1], t[0]+s[0])
    t[(i+1) % n] = min(t[(i+1) % n], t[i % n] + s[i % n])
for i in t:
    print(i)
