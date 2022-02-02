class RotateArray:
	def __init__(self,list):
		self.list=list
	def rotate(self,k):
		lenn=len(self.list)
		self.list.reverse()
		lenn2=lenn-1
		k1=k
		while k != lenn2 and k<lenn2:
			self.list[k],self.list[lenn2]=self.list[lenn2],self.list[k]
			k,lenn2=k+1,lenn2-1
		print(self.list)
		
def main():
		lin=list([1,2,3,4,5])
		R=RotateArray(lin)
		R.rotate(3)
if __name__=="__main__":
	main()