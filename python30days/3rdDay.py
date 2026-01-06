import math
#Exercise 3

#1. More variable and complex math i assume?
"""
age = 21
height = 190.6
complicated = 10j

b = int(input("Enter base of triangle: "))
h = int(input("Enter height of triangle: "))
areaOfTri = (b * h) / 2
print(f"The area of triangle is: {areaOfTri}")

sideA = int(input("Enter side A of triangle: "))
sideB = int(input("Enter side B of triangle: "))
sideC = int(input("Enter side C of triangle: "))
periOfTri = sideA + sideB + sideC
print(f"The perimeter of triangle is: {periOfTri}")

lenRect = int(input("Enter length of rect: "))
widthRect = int(input("Enter width of rect: "))
areaOfRect = lenRect * widthRect
periOfRect = 2 * (lenRect + widthRect)
print(f"The area of rect is: {areaOfRect}")
print(f"The perimeter of rect is: {periOfRect}")

r = int(input("Enter radius of circle: "))
pi = math.pi
areaOfCirc = pi * (r**2)
circumferenceOfCirc = 2 * pi * r
print(f"The area of circ is: {areaOfCirc}")
print(f"The perimeter of rect is: {circumferenceOfCirc}")

#the heck you mean calc x,y int and slope of y = 2x-2???
xInt = (0 + 2) / 2 
yInt = -2
grad = 2
#together...
x1, x2 = 2, 6
y1, y2 = 2, 10
m = (y2 - y1) / (x2 - x1) 
initialD = ((x2 - x1)**2) + ((y2 - y1)**2)
d = math.sqrt(initialD)
print(m - grad)

x = -3
y = x**2 + 6*x + 9
print(y)

pyLen = len("python")
pyDrag = len("dragon")
compLens = abs(pyLen - pyDrag)
print(f"Difference between these two creatures (in letter length) is: {compLens}")
#did 15 acidentally as well
if "on" in "python" and "on" in "dragon": {
    print("on IS within both")
}
else: {
    print("on NOT within both")
}

sentence = "I hope this course is not full of jargon"
checkJarg = "jargon"
if checkJarg in sentence: {
    print("Jargon IS in sentence")
}
else: {
    print("Jargon NOT in sentence")
}

whyJustWhy = float(len("python"))
againWhy = str(whyJustWhy)
print(type(againWhy))

subjectNo = 3
if subjectNo % 2 == 0: {
    print(f"Your number: {subjectNo} IS even")
}
else: {
    print(f"Your number: {subjectNo}, NOT even")
}

floorMoment =  float(7 // 3)
convMoment = int(7 // 3)
print(floorMoment)
print(convMoment)
if floorMoment == convMoment: {
    print("facts, they're the same")
}
else: {
    print("not quite they're not same")
}

typeA = type("10")
typeB = type(10)
if typeA == typeB: {
    print("Same")
}
else: {
    print("Different")
}
"""
typeAb = type(int(9.8))
typeBb = type(10)
if typeAb == typeBb: {
    print("Same")
}
else: {
    print("Different")
}