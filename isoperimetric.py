from sympy import *
from sympy.abc import x,L
y = Function('y')
z = Function('z')
z1 = z(x).diff(x)
y1 = y(x).diff(x)
k = 2
f = y1**2 + z1**2 - 4*x*z1 - 4*z(x)
g = y1**2 - x*y1 - z1**2
h = f+L*g
eq = diff(diff(h,y1),x)-diff(h,y(x))
yf = dsolve(eq,y(x),ics={y(0):0,y(1):1})
yf1 = yf.rhs.diff(x)

eq = diff(diff(h,z1),x)-diff(h,z(x))
zf = dsolve(eq,z(x),ics={z(0):0,z(1):1})
zf1 = zf.rhs.diff(x)

g = yf1**2 - x*yf1 - zf1**2
I = integrate(g,(x,0,1))-k
Lv = solve(I,L)
for i in Lv:
    print("L =",i)
    s = yf.rhs.subs(L,i)
    s1 = zf.rhs.subs(L,i)
    print(y(x),"=",s)
    print(z(x),"=",s1)