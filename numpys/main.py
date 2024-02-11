my_list = [1,2,3]
import numpy as np
arr = np.array(my_list)

# for matrix

my_mat = [[1,2,3],[4,5,6],[7,8,9]]
mat = np.array(my_mat)
# print(mat)

print(np.arange(0,10,3))
print(np.zeros((3,5)))

print(np.ones(3))
print(np.ones((3,5)))

print(np.linspace(0,5,100))  # 100 evenly spaced points from 0 to 5
print(np.eye(4))         # identity matrix

print(np.random.rand(5))  # 5 random numbers from 0 to 1
print(np.random.rand(5,5))  # 5x5 matrix of random numbers from 0 to 1
print("\n")
print(np.random.randn(5))  # 5 random numbers from standard normal distribution
print(np.random.randn(5,5))  # 5x5 matrix of random numbers from standard normal distribution
print("\n")

print(np.random.randint(1,100))  # random integer from 1 to 100 (not including 100)
print(np.random.randint(1,100,10))  # 10 random integers from 1 to 100 (not including 100)


arr=np.arange(25)
print(arr)
print(arr.reshape(5,5 )) # reshape to 5x5 matrix
print(arr.max()) # max value
print(arr.min()) # min value

print(arr.argmax()) # index of max value
print(arr.argmin()) # index of min value

print(arr.shape) # shape of array
print(arr.dtype) # data type of array

print(type(arr))

from numpy.random import randint
print(randint(2,10)) # random integer from 2 to 10 (not including 10)s
