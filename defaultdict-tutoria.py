from collections import defaultdict

n, m = map(int, input().split())
a = defaultdict(list)

for i in range(1, n+1):
    x = input().strip()
    a[x].append(i)

for i in range(m):
    x = input().strip()
    if x in a:
        print(' '.join(map(str, a[x])))
    else:
        print(-1)
