import math

def quadratic(a,b,c):
	A = b**2 - 4*a*c
	if A>= 0:
		x = (-b + math.sqrt(b*b - 4*a*c))/(2*a)
		y = (-b - math.sqrt(b*b - 4*a*c))/(2*a)
		return(x,y)
	else:
		return('Without solution')
	
a = int(input('a='))
b = int(input('b='))
c = int(input('c='))

print(quadratic(a,b,c))