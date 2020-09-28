from systemPlugins.core import *
from math import *
import statistics

def areaSquare(l):
	area = l**2
	print(theme["styles"]["answer"] + str(area))

def areaRectangle(l, w):
	area = w * l
	print(theme["styles"]["answer"] + str(area))

def areaTriangle(b, h):
	area = b * h
	area = area // 2
	print(theme["styles"]["answer"] + str(area))

def areaRhombus(D, d):
	area = D * d
	area = area // 2
	print(theme["styles"]["answer"] + str(area))

def areaTrapezoid(B, b, h):
	area = B * b
	area = area // 2
	area = area * h
	print(theme["styles"]["answer"] + str(area))

def areaRegularPolygon(P, a):
	area = P // 2
	area = area * a
	print(theme["styles"]["answer"] + str(area))

def areaCircle(r):
	area = r ** 2
	area = area * pi
	print(theme["styles"]["answer"] + str(area))

def areaRegularPentagon(s):
	s = s ** 2
	print(theme["styles"]["answer"] + str(1.720 * s))

def areaRegularHexagon(s):
	s = s ** 2
	print(theme["styles"]["answer"] + str(2.598 * s))

def areaRegularOctogon(s):
	s = s ** 2
	print(theme["styles"]["answer"] + str(4.828 * s))

def surfaceAreaCone(r, s):
	area = pi * r
	area = area * s
	print(theme["styles"]["answer"] + str(area))

def surfaceAreaSphere(r):
	area = r ** 2
	area = area * 4
	area = area * pi
	print(theme["styles"]["answer"] + str(area))

def surfaceAreaCube(s):
	area = s ** 2
	area *= 6
	print(theme["styles"]["answer"] + str(area))

def surfaceAreaRectangularPrism(a, b, c):
	first = 2 * a * b
	second = 2 * b * c
	third = 2 * a * c
	area = first + second + third
	print(theme["styles"]["answer"] + str(area))

def volumeCube(s):
	vol = s ** 3
	print(theme["styles"]["answer"] + str(vol))

def volumeParallelepiped(l, w, h):
	vol = l * w * h
	print(theme["styles"]["answer"] + str(vol))

def volumeRectangularPrism(b, h):
	vol = b * h
	print(theme["styles"]["answer"] + str(vol))

def volumeCylinder(r, h):
	vol = r ** 2
	vol = vol * pi
	vol = vol * h
	print(theme["styles"]["answer"] + str(vol))

def volumeCone(b, h):
	third = 1 / 3
	vol = third * b
	vol = vol * h
	print(theme["styles"]["answer"] + str(vol))

def volumeSphere(r):
	vol = r ** 3
	vol = vol * pi
	fraction = 4 / 3
	vol = vol*fraction
	print(theme["styles"]["answer"] + str(vol))

def perimeterSquare(s):
	per = 4 * s
	print(theme["styles"]["answer"] + str(per))

def perimeterRectangle(l, w):
	len = 2 * l
	wid = 2 * w
	per = len + wid
	print(theme["styles"]["answer"] + str(per))

def perimeterCircle(r=0, d=0):
	if r == 0:
		per = pi * d
	else:
		per = 2 * pi * r
	print(theme["styles"]["answer"] + str(per))

def mean(nums):
	print(theme["styles"]["answer"] + str(sum(nums) / len(nums)))

def median(nums):
	nums.sort()
	if len(nums) % 2 == 0:
		while len(nums) > 2:
			nums = nums[1:]
			nums = nums[:-1]
		median = nums[0] + nums[1]
		median = median // 2
		print(theme["styles"]["answer"] + str(median))
	else:
		while len(nums) > 1:
			nums = nums[1:]
			nums = nums[:-1]
		print(theme["styles"]["answer"] + str(nums[0]))

def mode(nums):
	print(theme["styles"]["answer"] + str(statistics.mode(nums)))

def range(nums):
	nums.sort()
	print(theme["styles"]["answer"] + str(nums[-1] - nums[0]))

def midpoint(x1, y1, x2, y2):
	x = x1 + x2
	x = x // 2
	y = y1 + y2
	y = y // 2
	print(theme["styles"]["answer"] + "(" + str(x) + ", " + str(y) + ")")

def distance(x1, y1, x2, y2):
	x = x2 - x1
	x = x ** 2
	y = y2 - y1
	y = y ** 2
	distance = x + y
	distance = sqrt(distance)
	print(distance)

def slope(x1, y1, x2, y2):
	y = y2 - y1
	x = x2 - x1
	slope = y / x
	slope = str(slope)
	if slope[-1] == "0" and slope[-2] == ".":
		i = 1
		while i < 3:
			slope = slope[:-1]
			i += 1
		print(slope)
	else:
		print(y)
		print(u"\u2014\u2014\u2014")
		print(x)

def distance(s, t):
	dis = s * t
	print("Traveled " + str(dis) + " u")

def speed(d, t):
	print(str(d//t) + " u/t")

def time(d, s):
	print(str(d//s) + " u")

def work(f, d):
	print(str(f * d) + " n-distanceUnit")

def force(m, a):
	print(str(m * a) + " newtons")

def mass(d, v):
	print(str(d * v) + " grams")

def density(m, v):
	print(str(m//v))

def quadForm(a, b, c):
    negB = b * -1
    bSqu = b ** 2
    second = 4 * a * c
    top = bSqu - second
    doubleA = a * 2
    top = reduced_sqrt(top)
    #print("")
    if (str(top).isalnum()) == False:
        topStr = str(negB) + "\u00B1" + str(top)
        i = 0
        while i < 5 - len(topStr):
            topStr = " " + topStr
            i+=1
        print(theme["styles"]["answer"] + topStr.center(8))

        print("\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014")
        i = 0
        doubleA = str(doubleA)
        while i < 5 - len(doubleA):
            doubleA = " " + doubleA
            i+=1
        print(doubleA.center(8))
    else:
        plus = int(negB) + int(top)
        plus = plus / (2*a)
        minus = int(negB) - int(top)
        minus = minus / (2*a)
        print(theme["styles"]["answer"] + "x = " + str(plus))
        print("x = " + str(minus))

def perfect_square(limit):
    accumulation_list = [1]
    index, increment = 0, 3
    while accumulation_list[-1] + increment <= limit:
        accumulation_list.append(accumulation_list[index] + increment)
        index += 1
        increment = 2 * index + 3
    return accumulation_list


def reduced_sqrt(n):
    """Print most reduced form of square root of n"""
    if n < 0:
        print('Negative input')
        return

    if sqrt(n).is_integer():
        #print(int(sqrt(n)))
        return n

    # Find perfect squares that are factors of n
    factors = [square for square in perfect_square(n/2) if n % square == 0 and square > 1]
    if len(factors) == 0:
        #print("\u221A" + str(n))
        return('\u221A' + str(n)) # Square root is irreducible
    else:
        a = int(sqrt(max(factors))) # Coefficient
        b = int(n / max(factors)) # Argument of the square root
        return(str(a) + '\u221A' + str(b)) # Reduced square root

def help():
	print(theme["styles"]["output"] + "Type formulas.calcs() to get a list of supported calculations and syntaxes or formulas.abbrList() to get a list of abbreviations. You can also input values out of order by directly specifying their values. Eg: quadForm(b=3, a=9, c=10)")

def abbrList():
	print(theme["styles"]["output"] + "l - Length")
	print("w - Width")
	print("h - Height")
	print("b - Base/Small Side")
	print("D - Large Diagonal")
	print("d - Small Diagonal/Diameter/Distance/Density")
	print("B - Large Side")
	print("P - Perimeter")
	print("a - apothem/Acceleration")
	print("r - Radius/Rate")
	print("s - Slant Height/Side")
	print("t - Time")
	print("u - units")
	print("f - Force")
	print("m - Mass")
	print("v - Volume")

def calcs():
	print(theme["styles"]["important"] + "Area")
	print(theme["styles"]["output"] + "areaSquare(<length>)")
	print("areaRectangle(<length>, <width>)")
	print("areaTriangle(<base>, <height>)")
	print("areaRhombus(<Large Diagonal>, <Small Diagonal>)")
	print("areaTrapezoid(<Large Side>, <Small Side>, <Height>)")
	print("areaRegularPolygon(<perimeter>, <apothem>)")
	print("areaRegularPentagon(<side>)")
	print("areaRegularHexagon(<side>)")
	print("areaRegularOctogon(<side>)")
	print("areaCircle(<radius>)")
	print("")
	print(theme["styles"]["important"] + "Surface Area")
	print(theme["styles"]["output"] + "surfaceAreaCone(<radius>, <Slant Height>)")
	print("surfaceAreaSphere(<radius>)")
	print("surfaceAreaCube(<side>)")
	print("surfaceAreaRectangularPrism(<side 1>, <side 2>, <side 3>)")
	print("")
	print(theme["styles"]["important"] + "Volume")
	print(theme["styles"]["output"] + "volumeCube(<side>)")
	print("volumeParallelepiped(<length>, <width>, <height>)")
	print("volumeRectangularPrism(<base>, <height>)")
	print("volumeCylinder(<radius>, <height>)")
	print("volumeCone(<base>, <height>)")
	print("volumeSphere(<radius>)")
	print("")
	print(theme["styles"]["important"] + "Perimeter")
	print(theme["styles"]["output"] + "perimeterSquare(<side>)")
	print("perimeterRectangle(<length>, <width>)")
	print("perimeterCircle(<radius>)")
	print("perimeterCircle(<diamter>)")
	print("")
	print(theme["styles"]["important"] + "Data")
	print(theme["styles"]["output"] + "mean([n1, n2, n3...])")
	print("median([n1, n2, n3...])")
	print("mode([n1, n2, n3...])")
	print("range([n1, n2, n3...])")
	print("")
	print(theme["styles"]["important"] + "Graphing between 2 points")
	print(theme["styles"]["output"] + "midpoint(x1, y1, x2, y2)")
	print("distance(x1, y1, x2, y2)")
	print("slope(x1, y1, x2, y2) ")
	print("")
	print(theme["styles"]["important"] + "Travel/Work")
	print(theme["styles"]["output"] + "distance(<speed>, <time>")
	print("speed(<distance, <time>)")
	print("time(<distance>, <speed>)")
	print("work(<force>, <distance>)")
	print("force(<mass>, <acceleration>)")
	print("mass(<density>, <volume>)")
	print("density(<mass>, <volume>)")
	print("")
	print(theme["styles"]["important"] + "Numerical Formulas")
	print(theme["styles"]["output"] + "quadForm(<a>, <b>, <c>)")