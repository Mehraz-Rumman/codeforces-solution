t= int(input())
for i in range(t):
    n = int(input())
    a = [int(i) % 2 for i in input().split()]
    if a.count(0) == n or (a.count(1) == n and n % 2 == 0):
        print("NO")
    else:
        print("YES")
