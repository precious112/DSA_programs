def revstring(s):
	if s== "":
		return ""
		
	revstrev=revstring(s[1:])
	first= s[0:1]
	result = revstrev + first
	return result
	
def main():
	print(revstring("Hello"))
if __name__ == "__main__":
	main()