for i in range(int(input())):
        p=int(input())
        r=list(map(int,input().split()))
        m=list(dict.fromkeys(r))

        print(len(m))


