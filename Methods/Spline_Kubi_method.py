import math
from sympy import symbols, Eq, solve

pi=math.pi
m = symbols('m')
ListM=[]
ListH=[]
ListD=[]
Listeq=[]
ListGama=[]
ListMiu=[]
MainMat=[]

def NaturalKubi(table,find):
    size= len(table["i"])
    ListM2 = ["Null"]*(size-3)
    fillH(table,size)
    fillGama(table,size)
    fillMiu(table,size)
    fillD(table,size)
    fillM(table,size)
    for i in range (size):
        line=[]
        for j in range (size):
            if i==0 or i==size-1 or j==0 or j==size-1:
                line.append(0)
            elif i==j:
                line.append(2)
            elif j==i+1:
                line.append(ListGama[i])
            elif i==j+1:
                line.append(ListMiu[i])
        MainMat.append(line)
    print('\nOur matrix is :')
    for i in range(size):
        print(MainMat[i])

    for i in range(size):
        maineq = 0
        eq = 0
        for j in range(size):
            eq_0 = 0
            eq_0 = MainMat[i][j] * ListM[j]
            eq += eq_0
        maineq = eq - ListD[i]
        Listeq.append(maineq)

    print(f'\nOur functions are : {Listeq}')

    for i in range(1, size-2):
        ListM2[i-1]=solve((Listeq[i], Listeq[i+1]), (symbols("m" + str(i)),symbols("m" + str(i+1))))
        ListM[0]=0
        ListM[1]=(ListM2[i-1][symbols("m" + str(i))])
        ListM[2]=(ListM2[i-1][symbols("m" + str(i+1))])
        ListM[3]=0
    print(f'\nOur M parameters are : {ListM}')


    for i in range(size-1):
        if table.get("x")[i]<find and find<table.get("x")[i+1]:
            xi=table.get("x")[i]
            xi_1=table.get("x")[i+1]
            fxi=table.get("y")[i]
            fxi_1=table.get("y")[i+1]
            indexi=i


    xi1_find=xi_1-find
    part1=(pow(xi1_find,3))*ListM[indexi]+(pow(xi1_find,3))*ListM[indexi+1]
    part_1=part1/(6*ListH[indexi])
    part_2=(((xi1_find)*fxi)+(find-xi)*fxi_1)/ListH[indexi]
    part3=((xi1_find)*ListM[indexi])+((find-xi)*ListM[indexi+1])
    part_3=(part3/6)*ListH[indexi]
    s=part_1+part_2-part_3
    print("\nNatural Kubin's solution:" ,s)


def fillH(table,size):
    for i in range(size-1):
        ListH.append(table.get("x")[i+1]-table.get("x")[i])
    print(f'\nOur H parameters are : {ListH}')



def fillMiu(table,size):
    for i in range(size-1):
        ListMiu.append(1-ListGama[i])
    ListMiu.append(None)
    print(f'\nOur Miu parameters are : {ListMiu}')



def fillM (table,size):
    for i in range (size):
        ListM.append(symbols("m" + str(i)))


def fillD(table,size):
    for i in range(size):
        if i==0 or i==size-1:
            ListD.append(0)
        else:
            x1=(6/(ListH[i-1]+ListH[i]))
            x2=((table.get("y")[i+1]-table.get("y")[i])/ListH[i])
            x3=((table.get("y")[i]-table.get("y")[i-1])/ListH[i-1])
            x=x1*(x2-x3)
            ListD.append(x)
    print(f'\nOur D parameters are : {ListD}')


def fillGama(table,size):
    for i in range(size-1):
        if i==0:
            ListGama.append(0)
        else:
            ListGama.append((ListH[i])/(ListH[i]+ListH[i-1]))
    print(f'\nOur Gemma parameters are : {ListGama}')


f0=1
fn=0


def FullKubi(table, find, f0,fn):
    size= len(table["i"])
    ListM2 = ["Null"]*(size-3)
    MainMat = []
    ListGama[0]=1
    ListMiu[size-1]=1
    ListD[0]=(6/ListH[0])*(((table.get("y")[1]-table.get("y")[0])/ListH[0])-f0)
    ListD[size-1]=(6/ListH[size-2])*(fn-((table.get("y")[size-1]-table.get("y")[size-2])/ListH[0]))
    for i in range(size):
        line = []
        for j in range(size):
            if i == j:
                line.append(2)
            elif j == i + 1:
                line.append(ListGama[i])
            elif i == j + 1:
                line.append(ListMiu[i])
            elif j > (i + 1) or i > (j + 1):
                line.append(0)
        MainMat.append(line)
    ListM.clear()
    fillM(table,size)
    Listeq.clear()

    for i in range(size):
        eq=0
        for j in range(size):
            eq_0=MainMat[i][j]*ListM[j]
            eq+=eq_0
        maineq=eq-ListD[i]
        Listeq.append(maineq)
    for i in range(size-3):
        ListM2[i]=solve((Listeq[i], Listeq[i+1],Listeq[i+2], Listeq[i+3]), (symbols("m" + str(i)),symbols("m" + str(i+1)),symbols("m" + str(i+2)),symbols("m" + str(i+3))))
    for i in range (size):
        ListM[i]=(ListM2[0][symbols("m" + str(i))])
    for i in range(size-1):
        if table.get("x")[i]<find and find<table.get("x")[i+1]:
            xi=table.get("x")[i]
            xi_1=table.get("x")[i+1]
            fxi=table.get("y")[i]
            fxi_1=table.get("y")[i+1]
            indexi=i
    xi1_find=xi_1-find
    part1=(pow(xi1_find,3))*ListM[indexi]+(pow(xi1_find,3))*ListM[indexi+1]
    part_1=part1/(6*ListH[indexi])
    part_2=(((xi1_find)*fxi)+(find-xi)*fxi_1)/ListH[indexi]
    part3=((xi1_find)*ListM[indexi])+((find-xi)*ListM[indexi+1])
    part_3=(part3/6)*ListH[indexi]
    s=part_1+part_2-part_3
    print("Full Kubin's solution:" ,s)
