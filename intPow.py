def intpow(n):
	if n == 0:
		return 1
	
	nPower2 = 2**n
	return intpow(n-1) *2
def main():
	l = int(input("enter number here"))
	P= intpow(l)
	print("the power", l,"of 2 is",str(P),".")
if __name__ == "__main__":
	main()
	