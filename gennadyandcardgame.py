n=input()
h=input().split()
count=0
for item in h:
    if item[0]==n[0] or item[1]==n[1]:
        count+=1
if count>0:
    print("YES")
else:
    print("NO")




