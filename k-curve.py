from TurtleWorld import *

world = TurtleWorld()
bob = Turtle()

def k_curve(n):
	if (n < 9):
		fd(bob,n)
		return
	else:
		k_curve(n/3)
		lt(bob,60)
		k_curve(n/3)
		rt(bob,120)
		k_curve(n/3)
		lt(bob,60)
		k_curve(n/3)

k_curve(99999999)
