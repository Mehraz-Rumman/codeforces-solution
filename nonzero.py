t = int(input())
for tc in range(t):
    n = int(input())
    count = 0
    l = list(map(int, input().split()))
    while (0 in l):
        i = l.index(0)
        l[i] += 1
        count += 1
    if (sum(l) == 0):
        count += 1
    print(count)

