


for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    if a[0]%2==0:
        print('1 \n1')
    elif n==1:
        print('-1')
    elif a[1]%2==0:
        print('1\n2')
    else:
        print('2\n1 2')

