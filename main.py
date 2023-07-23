n = int(input())
s = input()

a = s[:n]
b = s[n:]

a = sorted(map(int, a))
b = sorted(map(int, b))

if a[0] < b[0]:
    a, b = b, a

for i, j in zip(a, b):
    if i <= j:
        print("NO")
        raise SystemExit

print("YES")
