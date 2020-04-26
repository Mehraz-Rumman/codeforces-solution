n=map(int,input().split())
p=sorted(n)
a=0
b=0
c=0
for i in p:
    a=p[3]-p[1]
    b=p[3]-p[2]
    c=p[3]-p[0]
print(a,b,c)
