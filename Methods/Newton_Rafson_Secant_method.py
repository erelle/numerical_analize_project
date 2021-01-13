import math
import sympy

def FXR(fxr,fdxr,xr):
    return xr-(fxr/fdxr)

def dr(f):
    x = sympy.symbols('x')
    drx = sympy.diff(f)
    return drx

def dfx(i,polinom):
    x = sympy.symbols('x')
    f = dr(polinom(x))
    f_num = f.subs([(x, i)])
    return f_num

def NewtonRaphson(polinom,Range,epsilon):
    print("\n>>>>>>>>>>>>>> Newton Raphson >>>>>>>>>>")
    a=Range[0]
    b=Range[1]
    xr0=(a+b)/2
    fxr = polinom(xr0)
    fdxr = dfx(xr0,polinom)
    diff=1
    xr=xr0
    i=0
    while diff>epsilon:
        i+=1
        xr1=FXR(fxr,fdxr,xr)
        fxr = polinom(xr1)
        fdxr = dfx(xr1,polinom)
        diff=abs(xr1-xr)
        xr=xr1

        print(f'\nIteration number {i}')
        print(f"f'(x) = {xr} , f(x) = {fxr} , Xr = {fdxr} , Difference = {diff}")
        if i==10:
            break
    print("\nnum of iterations is: ",i,f"\nthe solution is: ({xr} , 0)",)
    return xr


def secant_method (polinom,Range,epsilon):
    print("\n>>>>>>>>>> Secant Method >>>>>>>>>>>")
    x0 = Range[0]
    x1 = Range[1]
    fx=polinom(x0)
    diff=1
    print(f'\nIteration number 1')
    print("xi=",x0, " xi+1=",x1, " f(xi)=",fx)
    i=1
    while diff>epsilon:
        i+=1
        nextx=(x0*polinom(x1)-x1*polinom(x0))/(polinom(x1)-polinom(x0))
        x0=x1
        fx= polinom(x0)
        diff=x1-nextx
        x1=nextx
        print(f'\nIteration number {i}')
        print("xi=",x0, " xi+1=",x1, " f(xi)=",fx)
    print("\nnum of iterations is: ",i,f"\nthe solution is : ({x1} , 0)")
    return x1

