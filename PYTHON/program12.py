import numpy
matrix1=numpy.matrix([[2,2,2],[2,2,2],[2,2,2]])
matrix2=numpy.matrix([[2,2,2],[2,2,2],[2,2,2]])
matrix3=numpy.add(matrix1,matrix2)
matrix4=numpy.subtract(matrix1,matrix2)
matrix5=numpy.matmul(matrix1,matrix2)
matrix6=2*matrix1
matrix7=numpy.transpose(matrix1)
print(matrix3)
print(matrix4)
print(matrix5)
print(matrix6)
print(matrix7)
