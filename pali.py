class Pali:
	def match(self,s,p):
		if len(p)==1:
			if p==s:
				print("q")
				return True
			else:
				print("f")
				return(False)
				
		else:
			if p[1]=="*":
				for i in s:
					if i ==p[0]:
						print("p")
						return True
						
					else:
						pass
				if p[0]==".":
					print("k")
					return True
				print("z")	
				return False
				
def main():
	s="aa"
	p=".*"
	pal=Pali()
	pal.match(s,p)
if __name__=="__main__":
	main()
					