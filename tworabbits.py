
for i in range(int(input())):
    x,y,a,b=map(int,input().split())

    c=(y-x)/(a+b)
    c=int(c)


    if (y-x)%(a+b)==0:
        print(c)

    else:
       print(-1)





