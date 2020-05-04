m,n=map(int,input().split())
if m==n:
    print(m*100, n*100+1)

elif n-m==1:
    print(m*100+99, n*100)

elif m==9 and n==1:
    print(9, 10)



else:
    print(-1)
