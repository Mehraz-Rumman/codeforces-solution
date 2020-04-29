m=int(input())
k=str(input())
d=k.count("D")
a=k.count("A")
if d>a:
    print("Danik")
elif d<a:
    print("Anton")
else:
    print("Friendship")

