from sympy import *

x = Symbol('x')

f, g = Symbol('f(x)'), Symbol('g(x)')

fx = x**3-50*x
gx = -x**4+88*x**2-241

func_all = fx - gx
q = solve(func_all)

lst_x = [i.evalf(5, chop=True) for i in q]
lst_y = [fx.subs(x, i) for i in lst_x]

for i, (x, y) in enumerate(zip(lst_x, lst_y), start=1):
    print(f'Точка пересечения {f} и {g}- {i}: ({x}, {y})')

plot(fx, gx)
plot(func_all)