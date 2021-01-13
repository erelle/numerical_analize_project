import math
import sympy
from math import e
import decimal
check=[]
checkdr=[]
exp=0.0001
e= 2.718281
Range=(-3,2)
def polinom(x):
    return x*4+x*3-3(x**2)
def Bisection_Method (polinom,Range,exp):
    a0=Range[1]
    b0=Range[0]
    if polinom(a0)*polinom(b0)>0:
        myfunc=dr(polinom(sympy.symbols('x')))
        diff=a0-b0
        error=int(-math.log((exp / (diff)),e) / (math.log(2,e)))+1
        i=b0
        while i<=a0:
            flag=0
            num=polinom(i)
            numi=i
            numdr=dfx(i)
            if numdr==0:
                flag+=1
                numdr=dfx(i-decimal.Decimal('0.1'))
            print(i, polinom(i),dfx(i))
            i+=decimal.Decimal('0.1')
            if(num*polinom(i)<0):
                check.append(float(numi))
                check.append(float(i))
            if(numdr*dfx(i)<0):
                if flag>0:
                    checkdr.append(float(numi-decimal.Decimal('0.1')))
                    checkdr.append(float(i))
                else:
                    checkdr.append(float(numi))
                    checkdr.append(float(i))
                flag=0
        print("main func: ")
        bl=1
        op(check,error,bl)
        print("dr func:")
        bl=0
        op(checkdr,error,bl)

def op(check,error,bl):
    length = int((len(check)))
    for j in range(0, length, 2):
        a = check[j + 1]
        b = check[j]
        diff = 1000
        c = (b + a) / 2
        count = 0
        temp = 10
        while diff > exp and count <= error:
            count += 1
            c0 = c
            c = (b + a) / 2
            fa = polinom(a)
            fb = polinom(b)
            fc = polinom(c)
            print(a, b, c, fa, fb, fc)
            if (fc * fa < 0):
                b = c
                diff = c0 - c + temp
                temp = 0
            elif (fc * fb < 0):
                a = c
                diff = c0 - c + temp
                temp = 0
            else:
                print("no point found")
                diff=0
        if bl == 0 and diff!=0 and polinom(c) == 0:
            print("result= ", c)
        if diff!=0 and bl==1:
            print("result= ", c)


def dr(f):
    x=sympy.symbols('x')
    drx=sympy.diff(f)
    #dri=derivative(f,i)
    return drx
def dfx(i):
    x = sympy.symbols('x')
    f2=polinom(x)
    f=dr(f2)
    f_num=f.subs([(x,i)])
    return f_num

Bisection_Method(polinom,Range,exp)