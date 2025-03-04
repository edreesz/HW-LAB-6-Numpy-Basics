import numpy as np
import time

#exercise 1
print("exercise 1 \n")
numbers = list(range(1000000))
start_time = time.perf_counter()
squared_numbers = [n**2 for n in numbers]
print(squared_numbers[:10])
end_time = time.perf_counter()
execution_time = end_time - start_time
print(f"Function execution time: {execution_time:.4f} seconds")

arr = np.arange(1000000)
start_time = time.perf_counter()
arr = arr ** 2
print(arr[:10])
end_time = time.perf_counter()
execution_time = end_time - start_time
print(f"Function execution time: {execution_time:.4f} seconds")
#Numpy is faster than list comprehension for large arrays because it alters the whole array without iterating over it.
print("exercise 2 \n")
matrix_a = np.random.randint(1, 10, size=(4, 4))
print("Matrix: \n", matrix_a)
print("size:" , matrix_a.size)
print("shape:", matrix_a.shape)
print("dimension:", matrix_a.ndim)


# exercise 3
print("exercise 3 \n")
size = 3
matrix_identity = np.eye(size)
print("\nMatrix Identity: \n", matrix_identity)
array_a = np.array(np.random.randint(1, 100, size = 20))
print("\nArray A: \n", array_a)


# exercise 4
print("exercise 4 \n")
matrix_b = np.random.randint(1, 25, size=(5, 5))
print("\nMatrix: \n", matrix_b)
print("\nThird row matrix: \n", matrix_b[2, :])
columns = [3,4]
print("\nLast 2 columns in the  matrix: \n", matrix_b[:, columns])
submatrix = matrix_b[1:4, 1:4]
print("\nSubmatrix: \n", submatrix)

# exercise 5
print("exercise 5 \n")
array_b = np.array(np.random.randint(1, 20, size = 20))
print("\n1D array: \n", array_b)
matrix_c = array_b.reshape(4, 5)
print("\nArray to matrix: \n", matrix_c)


'''exercise 1 

[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
Function execution time: 0.0989 seconds
[ 0  1  4  9 16 25 36 49 64 81]
Function execution time: 0.0066 seconds
exercise 2 

Matrix: 
 [[2 3 7 7]
 [1 4 5 4]
 [9 6 5 6]
 [7 2 9 8]]
size: 16
shape: (4, 4)
dimension: 2
exercise 3 


Matrix Identity: 
 [[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]

Array A: 
 [94 60 49 53 14 50 32 34 61 40 22 63 78 72 95 39 51 85 37 25]
exercise 4 


Matrix: 
 [[17  6 22  8  4]
 [19 12 21 20  1]
 [ 4 15 10 15 15]
 [ 4  4  4 12 24]
 [20  9 12  3 21]]

Third row matrix: 
 [ 4 15 10 15 15]

Last 2 columns in the  matrix: 
 [[ 8  4]
 [20  1]
 [15 15]
 [12 24]
 [ 3 21]]

Submatrix: 
 [[12 21 20]
 [15 10 15]
 [ 4  4 12]]
exercise 5 


1D array: 
 [19 16  1 11  9  8 14 18 17  5  9  5  1 19  2 13  4 17 17 13]

Array to matrix: 
 [[19 16  1 11  9]
 [ 8 14 18 17  5]
 [ 9  5  1 19  2]
 [13  4 17 17 13]]

Process finished with exit code 0
'''