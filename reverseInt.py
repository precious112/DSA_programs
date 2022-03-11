class ReverseInt:
	def reverse(self,x):
		j=str(x)
		s= list()
		for i in j:
			s.append(i)
		n= len(s)-1
		for i in range(len(s)-1):
			for i in range(n):
				if s[i]=='-':
					pass
				else:
					s[i],s[i+1]=s[i+1],s[i]
			n=n-1
		k=""
		for i in s:
			k=k+i
		j=k
		x= int(j)
		print(x)

def main():
	lin=-12345
	R=ReverseInt()
	R.reverse(lin)
if __name__=="__main__":
	main()			