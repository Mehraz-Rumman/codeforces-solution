n=int(input())
count=0
while n>0:
    if n>=5:
        p=n//5
        count+=p
        n=n%5
    elif n>=4:
        r=n//4
        count+=r
        n=n%4

    elif n>=3:
        s=n//3
        count+=s
        n=n%3

    elif n>=2:
        t=n//2
        count+=t
        n=n%2

    elif n==1:
        s=n//1
        count+=s
        n=n%1
print(count)



