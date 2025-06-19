n = int(input())

a = set(map(int, input().split()))
m = int(input())
c = set(map(int, input().split()))
b = a.difference(c)
print(len(b))
