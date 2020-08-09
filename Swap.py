def Swap(S):
	if S=="":
		print("nothing to swap")
	b=[]	
	a=[]
	x=0
	j= 2
	k=list(S)
	
	for i in range(len(k)):
		if len(k)%2==0:
			b=k[x:j]
			b.reverse()
			a=a+b
			x+=2
			j+=2
		else:
			print("enter an even numbered String")
	
	print(*a)
		
def main():
	x= input("Enter character here:")
	l = Swap(x)
	
if __name__ == "__main__":
	main()
			