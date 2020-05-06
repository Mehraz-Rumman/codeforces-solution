for _ in range(int(input())):
	n=int(input())
	if(n%4!=0):
		print("NO")
	else:
		even=[2*i for i in range(1,(n//2)+1)]
		odd=[2*i-1 for i in range(1,(n//2)+1)]
		odd[-1]+=(n//2)
		print("YES")
		print(*(even+odd))
        
