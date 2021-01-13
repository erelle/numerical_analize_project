from Methods import Newton_Rafson_Secant_method , Romberg_Simpson_methods, Spline_Kubi_method,Jacobs_Zaidel_methods
import math
import sympy as sym



print('///////////////// First Question : Question 5 /////////////////')

e=math.exp(1)
epsilon=0.00001


def Qs5a(x):
    return (sym.sin(2*e**(-2*x)))/(2*x**3+5*x**2-6)

def Qs16a(x):
    return (x**2*e**(-x**2+5*x-3))*(3*x-5)


def Newton_secant(f,domain,epsilon):
    newton_rafson=Newton_Rafson_Secant_method.NewtonRaphson(f,domain,epsilon)
    secant=Newton_Rafson_Secant_method.secant_method(f,domain,epsilon)
    print(f"\nThe difference between the two is : {secant - newton_rafson}")

def Romberg_Simpson(f,a,b,n):
    romberg=Romberg_Simpson_methods.romberg(f,a,b,n)
    simpson=Romberg_Simpson_methods.simpson(f,a,b,n)
    print(f"\nThe difference between the two is : {romberg - simpson}")


def Jacobs_Zaidel(matrix,solution):
    jacobs=Jacobs_Zaidel_methods.Jacobs(matrix,solution)
    zaidel=Jacobs_Zaidel_methods.Zaidel(matrix,solution)
    print(f"\nThe difference between the two is : \nx : {jacobs[0] - zaidel[0]}"
          f"\ny : {jacobs[1] - zaidel[1]}"
          f"\nz : {jacobs[2] - zaidel[2]}")



print('\n///////////////// Question 5 - Secation A ///////////////////'
      '\n\n!!!!!!!! we are going to use Newton Rafson and Secant methods to solve this problem .')
domain5=(-1.1,2)
Newton_secant(Qs5a,domain5,epsilon)

print('\n///////////////// Question 5 - Secation B /////////////////'
      '\n\n!!!!!!!! we are going to use Romberg and Simpson methods to solve this problem .')

Romberg_Simpson(Qs5a,-0.5,0.5,4)


print('\n///////////////// Second Question : Question 16 /////////////////')


print('\n///////////////// Question 16 - Secation A /////////////////'
      '\n\n!!!!!!! we are going to use Newton Rafson and Secant methods to solve this problem .')
domain16=(0,3)

Newton_secant(Qs16a,domain16,epsilon)


print('\n///////////////// Question 16 - Secation B /////////////////'
      '\n\n!!!!!!!! we are going to use Romberg and Simpson methods to solve this problem .')

Romberg_Simpson(Qs16a,0.5,1,4)



print('\n///////////////// Third Question : Question 19 ///////////////// '
      '\n\n!!!!!!!! we are going to use Jacob and Zaidel methods to solve this problem .')

matrix=[[5,1,10],[10,8,1],[4,10,-5]]

sol=[1.5,-7,2]

Jacobs_Zaidel(matrix,sol)

print('\n///////////////// Third Question : Question 20 ///////////////// '
      '\n\n!!!!!!!! we are going to use Jacob and Zaidel methods to solve this problem .')

matrix=[[10,8,1],[4,10,-5],[5,1,10]]

sol=[-7,2,1.5]
Jacobs_Zaidel(matrix,sol)


print('\nSixth Question : Question 40'
      '\n\nwe are going to use Spline Natural Kubi methods to solve this problem .')

find=(0.25)
table={"i":[0,1,2,3],"x":[0.1,0.2,0.3,0.4],"y":[-0.62049958,-0.28398668,0.0060095,0.24842440]}

spline_kubi=Spline_Kubi_method.NaturalKubi(table,find)


