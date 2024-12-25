#Write a Python program to compute following computation on matrix:
#a)Addition of two matrices b) Subtraction of two matrices
#c) Multiplication of two matrices d) Transpose of a matrix
import numpy as np
print ("for matrix1")
n= int(input("Enter the no. of rows: "))
m=int(input("Enter the no. of columns: "))
print("Enter the elements row wise: ")
matrix1= [ ]
for i in range (n):
 a=[ ]
 for j in range(m):
  v=int(input( ))
  a.append(v)
 matrix1.append(a)
print(matrix1)
print("for matrix2")
n1=int(input("Enter the no. of rows: "))
m1=int(input("Enter the no. of columns: "))
print("Enter the elements row wise: ")
matrix2=[ ]
for i in range (n1):
 a1=[ ]
 for j in range(m1):
  v=int(input( ))
  a1.append(v)
 matrix2.append(a1)
print(matrix2)
print("Addition of the two matrices is :\n",np.add(matrix1,matrix2))
print("Subtraction of the two matrices is :\n",np.subtract(matrix1,matrix2))
print("Multiplication of the two matrices is :\n",np.multiply(matrix1,matrix2))
print("Division of the two matrices is :\n",np.divide(matrix1,matrix2))
print("Transpose of matrix 1 is:\n ",np.transpose(matrix1))
print("Transpose of matrix 2 is:\n ",np.transpose(matrix2))