n=map(int,input().split())
p=list(n)
if p[0]>p[1]:
    print("NO")
elif p[0]>p[2]:
    print("NO")
else:
    print("YES")

