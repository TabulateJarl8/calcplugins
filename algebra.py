from sympy.solvers import solve as solveeq
from sympy import Symbol, Eq, sympify, Poly, div
from sympy import simplify as ssimplify
from sympy import expand as sexpand
from sympy import factor as sfactor
import re
from systemPlugins.core import theme
from decimal import Decimal
import mpmath

def toValidEqn(eqn):
	# Replace `[number][coefficient]` with `[number]*[coefficient]` and )( with )*(. E.g. (3x)(2) -> (3*x)*(2)
	eqn = eqn.replace(" ", "").replace("^", "**").replace('pi', '@') # also replace pi with @ to prevent changing to p*i
	eqn = re.sub(r"((?:[a-zA-Z0-9]+)|(?:[a-zA-Z]\w*\(\w+\)))((?:[a-zA-Z]\w*)|\()", r"\1*\2", eqn)
	eqn = re.sub(r'(\))((?:[a-zA-Z]\w*)|\()', r'\1*\2', eqn)
	mathFunctions = '|'.join([attribute for attribute in dir(mpmath) if not attribute.startswith("_")])
	eqn = re.sub('(' + mathFunctions + '){1}\*\(', r"\1(", eqn)
	eqn = eqn.replace('@', 'pi') # restore pi
	return eqn

def solve(eqn, *args, **kwargs):

	# Equation is equal to 0
	if eqn.count("=") == 0:
		eqn = [eqn, '0']
	# Comparing expressions using =
	elif eqn.count("=") == 1:
		eqn = eqn.split("=")
	# Comparing expressions using ==
	elif eqn.count("=") == 2:
		# Test that the 2 equal signs are next to each other

		if eqn.find("==") != -1:
			eqn = eqn.split("==")
		else:
			# Two equal signs are not next to each other, terminate
			print(theme['styles']['error'] + "Equation can only have = or == to signify equilvalance between two expressions" + theme['styles']['normal'])
			return
	else:
		# = or == not in string
		print(theme['styles']['error'] + "Equation can only have = or == to signify equilvalance between two expressions" + theme['styles']['normal'])
		return

	# Convert to valid equation, see toValidEqn
	eqn = list(map(toValidEqn, eqn))

	if "debug" in kwargs:
		print(eqn)

	# Solve
	sympy_eq = sympify("Eq(" + eqn[0] + ", " + eqn[1] + ")")

	# TODO: Single letter variable mode
	solved = [solveeq(sympy_eq, sym, dict=True) for sym in sympy_eq.free_symbols]

	# Flatten list
	flat_list = [item for sublist in solved for item in sublist]

	# Convert symbol objects to strings
	flat_list = [{str(key): str(value) for key, value in solution.items()} for solution in flat_list]
	# Print answers
	requested_answers = []
	if len(args) == 0:
		args = ('x',)

	for arg in args:
		requested_answers.extend([str(arg) + ' = ' + solution[str(arg)] for solution in flat_list if str(arg) in solution])

	return '\n'.join(requested_answers)

def simplify(eqn):
	return ssimplify(toValidEqn(eqn))

def expand(eqn):
	return sexpand(toValidEqn(eqn))

def factor(eqn):
	return sfactor(toValidEqn(eqn))

def rational(eqn, numbers_to_test, debug=False):
	# Find rational zeros
	if isinstance(numbers_to_test, (int, float, Decimal)):
		numbers_to_test = [numbers_to_test]
	numbers_to_test = [Decimal(str(i)) for i in list(numbers_to_test)]
	if not isinstance(eqn, list):
		# Eqn is polynomial equation; extract coefficients
		eqn = toValidEqn(eqn)
		polynomial = Poly(sympify("Eq(" + eqn + ", 0)"))
		coeffs = [Decimal(str(i)) for i in polynomial.coeffs()]
	else:
		# Eqn is list of coefficients
		coeffs = [Decimal(str(i)) for i in eqn]

	positive_numbers_to_test = [Decimal(str(abs(i))) for i in list(numbers_to_test)]
	negative_numbers_to_test = [Decimal(str(-abs(i))) for i in list(numbers_to_test)]

	zeros = []

	# Po
	for number in positive_numbers_to_test + negative_numbers_to_test:
		stack = number * coeffs[0]
		for i in range(1, len(coeffs)):
			stack += coeffs[i]
			stack *= number
		if debug == True:
			print(stack)
		if stack == 0:
			zeros.append(number)
	return '\n'.join([str(ans) for ans in zeros])

def polydiv(n, d, domain='QQ'):
	return div(toValidEqn(n), toValidEqn(d))

def synthetic(divisor: int, dividend: str, quiet=False):
	eqn = toValidEqn(dividend)
	eqn = sympify("Eq(" + eqn + ", 0)")
	symbol = list(eqn.free_symbols)[0]
	eqn = Poly(eqn, symbol)
	coeffs = eqn.all_coeffs()
	current = coeffs[0]

	new_coeffs = []
	middle_numbers = ['']

	for coefficient in coeffs[1:]:
		new_coeffs.append(current)
		current = Decimal(str(divisor)) * Decimal(str(current))
		middle_numbers.append(current)
		current += Decimal(str(coefficient))

	coefficient_printable = ''
	middle_numbers_printable = ''
	new_coeffs_printable = ''
	for coef, num, new_coef in zip(coeffs, middle_numbers, new_coeffs + [current]):
		coef = str(coef)
		num = str(num)
		new_coef = str(new_coef)

		# pad numbers with space
		max_length_number = max(len(coef), len(num), len(new_coef))

		coef = coef.rjust(max_length_number)
		num = num.rjust(max_length_number)
		new_coef = new_coef.rjust(max_length_number)

		coefficient_printable = coefficient_printable + '    ' + coef
		middle_numbers_printable = middle_numbers_printable + '    ' + num
		new_coeffs_printable = new_coeffs_printable + '    ' + new_coef

	# remove extra whitespace
	coefficient_printable = '|' + coefficient_printable[4:]
	middle_numbers_printable = '|' + middle_numbers_printable[4:]
	new_coeffs_printable = ' ' + new_coeffs_printable[4:]

	if not quiet:
		print(theme['styles']['normal'] + str(divisor) + '  ' + coefficient_printable)

		print((len(str(divisor)) + 2) * ' ' + '\u001b[4m' + middle_numbers_printable + '\u001b[0m')

		print(theme['styles']['normal'] + (len(str(divisor)) + 2) * ' ' + new_coeffs_printable)

		print()

		degree = len(new_coeffs) - 1

		equation = ''
		for coef in new_coeffs:
			if coef != 0:
				# skip coefs that are 0
				if degree != len(new_coeffs) and coef > 0:
					# not first number and positive
					equation += '+'
				equation += str(coef) if coef != 1 else ''
				if degree != 0:
					equation += str(symbol)
				if degree > 1:
					equation += f'^{degree}'
			degree -= 1

	return equation.lstrip('+')


def help():
	print(theme['styles']['prompt'] + "algebra.solve(eqn, *, debug=False) - Solves algebraic equation." + theme['styles']['normal'])
	print()
	print(theme['styles']['important'] + "eqn" + theme['styles']['normal'] + " - The equation that you want to solve. Example: " + theme['styles']['input'] + "2x-3=7" + theme['styles']['normal'] + ".")
	print(theme['styles']['important'] + "*" + theme['styles']['normal'] + " - Any number of strings of the variables you would like to solve for. For example, if you wanted to solve for x and y, you would give the function " + theme['styles']['input'] + "\"x\", \"y\"" + theme['styles']['normal'] + ".")
	print(theme['styles']['important'] + "debug" + theme['styles']['normal'] + " - Print debug information. Defaults to False." + theme['styles']['normal'])
	print()
	print(theme['styles']['important'] + "Note: " + theme['styles']['normal'] + "this function does not currently support multiple variables next to each other, for example, " + theme['styles']['input'] + "xy" + theme['styles']['normal'] + ", because we cannot detect the difference between that and something like " + theme['styles']['input'] + "sqrt" + theme['styles']['normal'] + ". To use these types of variables, please signify the multiplication, for example, writing " + theme['styles']['input'] + "x*y" + theme['styles']['normal'] + " instead of " + theme['styles']['input'] + "xy" + theme['styles']['normal'] + ".")
	print()
	print()
	print(theme['styles']['prompt'] + "algebra.simplify(eqn) - Simplifies the given equation." + theme['styles']['normal'])
	print()
	print()
	print(theme['styles']['prompt'] + "algebra.expand(eqn) - Expands a polynomial expression. " + theme['styles']['normal'])
	print("Example: " + theme['styles']['input'] + "(x+1)^2 " + theme['styles']['normal'] + "->" + theme['styles']['input'] + " x + 2*x + 1" + theme['styles']['normal'])
	print()
	print()
	print(theme['styles']['prompt'] + "algebra.factor(eqn) - Factors a polynomial into irreducible factors. " + theme['styles']['normal'])
	print("Example: " + theme['styles']['input'] + "x^3 - x^2 + x - 1 " + theme['styles']['normal'] + "->" + theme['styles']['input'] + " (x - 1)*(x**2 + 1)" + theme['styles']['normal'])
	print()
	print()
	print(theme['styles']['prompt'] + "algebra.rational(eqn, numbers_to_test, debug=False) - Finds the rational zeros of a polynomial function via synthetic division." + theme['styles']['normal'])
	print()
	print(theme['styles']['important'] + "eqn" + theme['styles']['normal'] + " - The polynomial equation, or a list of coefficients of the polynomial equation. Example: " + theme['styles']['input'] + "x^3+2x^2-5x-6" + theme['styles']['normal'] + ".")
	print(theme['styles']['important'] + "numbers_to_test" + theme['styles']['normal'] + " - Possible rational zeros. This can be a list of numbers, or a single number.")
	print(theme['styles']['important'] + "debug" + theme['styles']['normal'] + " - Print debug information. Defaults to False." + theme['styles']['normal'])
	print()
	print()
	print(theme['styles']['prompt'] + "algebra.polydiv(numerator, denominator, domain=\'QQ\') - Divide polynomials. Returns (solution, remainder)" + theme['styles']['normal'])
	print("Example: " + theme['styles']['input'] + "(3x^2-2x+1), (x-1) " + theme['styles']['normal'] + "->" + theme['styles']['input'] + " (3*x + 1, 2)" + theme['styles']['normal'])
	print()
	print()
	print(theme['styles']['prompt'] + "algebra.synthetic(divisor: int, dividend: str, quiet=False) - Perform synthetic division on a polynomial. Returns the resulting equation" + theme['styles']['normal'])
	print("Example: " + theme['styles']['input'] + "3, \"x^3-2x^2-5x+6\" " + theme['styles']['normal'] + "->" + theme['styles']['input'] + " x^3+x^2-2x" + theme['styles']['normal'])

