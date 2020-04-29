r,b=map(int,input().split())
countdiff=0
countsame=0
while r>0 and b>0:
    r-=1
    b-=1
    countdiff+=1

    if r>1 and b==0:
        countsame+=r//2
    elif b>1 and r==0:
        countsame+=b//2
print(countdiff, countsame)

