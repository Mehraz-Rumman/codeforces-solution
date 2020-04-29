n=int(input())
a=str(input())
z=a.count("z")
m=a.count("n")

for i in range(m):
    print("1",end=" ")
for i in range(z):
    print("0",end=" ")