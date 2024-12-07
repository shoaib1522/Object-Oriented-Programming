class Polynomial:
	pass

def createPolynomial(degree):
	p = Polynomial()
	p.degree = degree
	p.coefficient = [0] * (p.degree+1)
	p.variable = 'x'
	return p

def setCoefficient(polynomial, power, coefficient):
	polynomial.coefficient[power] = coefficient

def printPolynomail(polynomial):
	i = polynomial.degree
	while i >= 0:
		if polynomial.coefficient[i] != 0:
			print(polynomial.coefficient[i], end='')
			print(polynomial.variable, end='')
			print('^', end='')
			print(i, end=' ')
			print('+' if polynomial.coefficient[i-1] > 0 else '', end=' ')
		i = i-1
	print()

def value(polynomial, x):
	val = 0
	i = polynomial.degree
	while i >= 0:
		val = val + polynomial.coefficient[i] * pow(x, i)
		i = i-1
	return val

def main():
	e = createPolynomial(3)
	setCoefficient(e, 3, -2)
	setCoefficient(e, 2, 5)
	setCoefficient(e, 0, -1)
	printPolynomail(e)
	print(value(e, 1))
	print(value(e, 2))
	print(value(e, -5))

main()
