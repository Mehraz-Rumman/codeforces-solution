for i in range(int(input())):
    a,b,c,n=map(int,input().split())
    k=a+b+c+n
    if k%3==0 and max(a,b,c)<=k/3:
        print("YES")
    else:
        print("No")
        



