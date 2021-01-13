import numpy


# Function to get max element
def maxelement(arr):
    temp=[]
    no_of_rows = len(arr)
    no_of_column = len(arr[0])

    for i in range(no_of_rows):

        # Initialize max1 to 0 at beginning
        # of finding max element of each row
        max1 = 0
        for j in range(no_of_column):
            if arr[i][j] > max1:
                max1 = arr[i][j]
                maxj=j
                maxi=i

        temp=arr[maxi]
        arr[maxi]=arr[maxj]
        arr[maxj]=temp

    print(arr)





def Jacobs(matrix, solution):
    print("\n>>>>>>>>>>>>> Jacobs >>>>>>>>>>>>>\n ")
    print('arranging the matrix to be a dominant matrix\n')
    maxelement(matrix)
    e=0.001
    x,y,z=0,0,0
    dif=1
    while dif>e:
        x0,y0,z0=x,y,z
        i=0
        x=(solution[0]-matrix[i][1]*y0-matrix[i][2]*z0)/matrix[i][0]
        i+=1
        y=(solution[1]-matrix[i][0]*x0-matrix[i][2]*z0)/matrix[i][1]
        i+=1
        z=(solution[2]-matrix[i][0]*x0-matrix[i][1]*y0)/matrix[i][2]
        print("x: ", x, ",y: ", y, ",z: ",z)
        dif=abs(x-x0)
    print(f"x - x0 = {dif}")
    print(f"\nThe Jacobs solution is : (x : {x} , y : {y} , z : {z} )")

    solution = [x, y, z]
    return solution



def Zaidel(matrix, solution):
    print("\n>>>>>>>>>>>>>>> Zaidel >>>>>>>>>>>>>>>>\n ")
    print('arranging the matrix to be a dominant matrix\n')
    maxelement(matrix)
    e = 0.001
    x, y, z = 0, 0, 0
    dif = 1
    while dif > e:
        x0, y0, z0 = x, y, z
        i = 0
        x = (solution[0] - matrix[i][1] * y0 - matrix[i][2] * z0) / matrix[i][0]
        i += 1
        y = (solution[1] - matrix[i][0] * x - matrix[i][2] * z0) / matrix[i][1]
        i += 1
        z = (solution[2] - matrix[i][0] * x - matrix[i][1] * y) / matrix[i][2]
        print("x: ", x, ",y: ", y, ",z: ", z)
        dif = abs(x - x0)
    print(f"x - x0 = {dif}")
    print(f"\nThe Zaidel solution is : (x : {x} , y : {y} , z : {z} )")

    solution=[x,y,z]
    return solution

