
for i  in range(int(input())):
    a,b=map(int,input().split())
    c=abs(a-b)
    k=0
    k=k+c//5
    c=c%5
    k=k+c//2
    c=c%2
    k=k+c
    print(k)