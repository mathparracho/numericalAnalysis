#aula 2

import sympy as sp

def func(n):
    x = sp.Symbol('x')

    func = (x**4) + 2*(x**3) - x - 1
    funcX = func.evalf(subs = {x : n})

    der = sp.diff(func)
    derX = der.evalf(subs = {x : n})

    nexrec = n - (funcX/derX)

    return funcX,derX,nexrec

def main(inivalue,iteraçoes):
    print("x value ----------|", "f(x) -------------|", "f'(x) -------------|", "x(n+1)")
    for i in range(iteraçoes):
        funcX, derX, nexrec = func(inivalue)
        print("%0.15f | " % inivalue,end="")
        print(funcX, " | ", derX, " | ", nexrec)
        inivalue = nexrec
        

main(1, 10)