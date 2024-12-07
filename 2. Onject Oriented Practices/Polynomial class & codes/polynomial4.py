class Polynomial:
	def __init__(self, degree):
		self._deg = degree
		self._coef = [0] * (self._deg+1)
		self._var = 'x'
	
	def __str__(self):
		s = ""
		i = self._deg
		while i >= 0:
			if self._coef[i] != 0:
				if i < self._deg and self._coef[i] > 0:
					s = s + '+ '
				else:
					s = s + '- '
				s = s + str(abs(self._coef[i]))
				s = s + self._var
				s = s + '^'
				s = s + str(i)
			i = i-1
		return s

	def __len__(self):
		return _deg

	def __getitem__(self, power):
		return self._coef[power]

	def __setitem__(self, power, coeffient):
		self._coef[power] = coeffient

	def __add__(self, rhs):
		# code it yourself

	def value(self, x):
		val = 0
		i = self._deg
		while i >= 0:
			val = val + self._coef[i] * pow(x, i)
			i = i-1
		return val

def main():
	e = Polynomial(3)
	e[3] = -2
	e[2] = 5
	e[0] = -1
	print(e)
	print(e.value(1))
	print(e.value(x=5))
	print(e.value(-2))

main()
