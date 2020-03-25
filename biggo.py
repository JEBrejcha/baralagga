from math import sqrt
import sympy as sy

#Uppgift 2
def h(t):
    return t*(9 - 4.91*t)
print("Kvadartisk funktion : (a * x^2) + b*x + c")
a = float(-4.91)
b = float(9)
c = float(-2)

r = b**2 - 4*a*c

if r > 0:
    num_roots = 2
    x1 = (((-b) + sqrt(r))/(2*a))
    x2 = (((-b) - sqrt(r))/(2*a))
    print("Det finns två rötter: %f and %f" % (x1, x2))
elif r == 0:
    num_roots = 1
    x = (-b) / 2*a
    print("There is one root: ", x)
else:
    num_roots = 0
    print("No roots, discriminant < 0.")
    exit()
if x1 > x2:
    t = x1
    round(t, 3)
else:
    t = x2
    t = "{:.2f}".format(t)
    t = float(t)
print('Bollen är i hålet efter',t,'antal sekunder')
#Uppgift 3
def s(t):
    return(8*t)
print('Bollen har färdats lodrätt',s(t),'meter')
#Uppgift 4
t = sy.symbols("t")
f = x**2
f

