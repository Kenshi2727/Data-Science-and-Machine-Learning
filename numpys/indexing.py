import numpy as np
arr = np.arange(0, 11)
print(arr)
print(arr[8])
print(arr[1:5])
print(arr[0:5])
print(arr[:6])
print(arr[5:])
arr[0:5]=100
print(arr)

slice_of_arr= arr[0:6]
print(slice_of_arr)
slice_of_arr[:]=99
print(slice_of_arr)

arr_copy=arr.copy()
print(arr_copy)

# 2D array also known as matrix

arr_2d = np.array([[5,10,15],[20,25,30],[35,40,45]]) #passed nested list
print(arr_2d)
print(arr_2d[0][0])#row and column
print(arr_2d[0])#row
print(arr_2d[1][1])
print(arr_2d[1,1])#same as above
print(arr_2d[:2,1:])#grab 10,15,25,30
print(arr_2d[2])#grab 35,40,45
print("\n")
print(arr_2d[1:3,:2])
print("\n")
print(arr_2d[:2,:2])

bool_arr = arr_2d > 5
print(bool_arr)

arr1=np.arange(1,11)
print(arr1[arr1%2==0])

arr2=np.arange(50).reshape(5,10)
print(arr2)