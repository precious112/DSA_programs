def factorial(n):
	if n==0:
		return 1
	elif n==1:
		return 1
	y=[]
	for i in range(n):
		while n !=0:
			y= y + [n]
			n -= 1
	j=1	
	for i in y:
		j= j*i
	return j
	
	
		
		
	
	factorial(n-1)*n
	
def main():
	x= int(input("Enter num here"))
	f= factorial(x)
	print("factorial of x is",f)
if __name__=="__main__":
	main()
			
			
			