#code draws a tree by recursion
import turtle

def drawBranch(t,branchWidth,lenght,colour):
	if lenght<5:
		return
	
	
	if lenght>5:
		t.pensize(branchWidth)
		t.color(colour)
		t.forward(lenght)
		t.left(30)
		t.color('green')
		t.fillcolor('green')
		t.begin_fill()
		t.circle(3)
		t.end_fill()
		drawBranch(t,branchWidth-1,lenght-10,colour)
		t.right(60)
		drawBranch(t,branchWidth-1,lenght-10,colour)
		t.left(30)
		t.backward(lenght)



def main():
	t=turtle.Turtle()
	screen=t.getscreen()
	t.speed(200)
	t.penup
	t.goto(0,0)
	t.pendown
	t.setheading(90)
	drawBranch(t,7,80,'brown')
	screen.exitonclick()
if __name__=="__main__":
	main()

	
		