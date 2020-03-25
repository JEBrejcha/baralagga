from math import sqrt


# Uppgift 2 --------
def h(t):
    return t * (9 - 4.91 * t)


# Kvadartisk funktion : (a * x^2) + b*x + c")
a = float(-4.91)
b = float(9)
c = float(-2)

r = b ** 2 - 4 * a * c

if r > 0:
    num_roots = 2
    x1 = (((-b) + sqrt(r)) / (2 * a))
    x2 = (((-b) - sqrt(r)) / (2 * a))
 
if x1 > x2:
    t = x1
    t = "{:.2f}".format(t)
else:
    t = x2
    t = "{:.2f}".format(t)
    t = float(t)
print('Bollen är i hålet efter', t, 'antal sekunder')


# Uppgift 3 --------
def s(t):
    return (8 * t)


print('Bollen har färdats lodrätt', s(t), 'meter')

# Uppgift 4 --------
import sympy as sy

t = sy.Symbol('t')

# Hastigheten Horisontellt
dst = (sy.diff(s(t), t))

# Hastigheten Vertikalt
(sy.diff(h(t), t))


def dh(t):
    return (sy.diff(h(t), t))


ddht = (dh(t).subs(t, 1.57))
ddht = "{:.2f}".format(ddht)

# Resulterande hastighet
v = sqrt((float(ddht) ** 2) + (dst ** 2))
v = "{:.2f}".format(v)
print('Den resulternade hastighten är', v, 'm/s')

# Uppgift 5 --------

# Integralen s
(sy.integrate(s(t), t))


def ins(t):
    return (sy.integrate(s(t), t))


inst = (ins(t).subs(t, 1.57))

# Integralen h
(sy.integrate(h(t), t))


def inh(t):
    return (sy.integrate(h(t), t))


inht = (inh(t).subs(t, 1.57))

#Arean under
au = inst*inht
au = "{:.2f}".format(au)
print('Arean under är',au,'m**2')