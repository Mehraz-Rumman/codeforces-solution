for i in range(int(input())):
    a, b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    print(min(b, sum(c)))