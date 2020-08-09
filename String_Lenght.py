def StringLength(S):
	if S=="":
		return 0
	y= 0	
	for i in S:
		i = S[y]
		y += 1
	return y
	
def main():
	x= (input("enter character here"))
	l = StringLength(x)
	print(StringLength(x))
if __name__ == "__main__":
	main()