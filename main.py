n, k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse = True)

for k in range(3) :
    if a[k] <= b[k] :
        a[k], b[k] = b[k], a[k]
    else :
        break
print(sum(a))