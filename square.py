
for i in range(int(input())):
    a,b=sorted(map(int,input().split()))
    c,d=sorted(map(int,input().split()))
    if a+c==b==d:
        print("YES")
    else:
        print("NO")
