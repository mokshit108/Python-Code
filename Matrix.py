from numpy import *
arr1 = array([
    [1,2,3,6],
    [4,5,6,7]
])
#print(arr1)
#print(arr1.ndim)
#print(arr1.dtype)
#print(arr1.shape)
#print(arr1.size)
#to convert 2dim to 1dim
'''arr2 = arr1.flatten()
print(arr2)
arr3 = arr2.reshape(3,4)
print(arr3)
arr3 = arr2.reshape(2,2,3)
print(arr3)
'''
#print(arr1)
'''m = matrix(arr1)
print(m)'''
m1 = matrix('1 2 3; 6 4 5; 1 6 7 ')
m2 = matrix('1 2 3; 6 8 5; 2 6 7 ')
m3 = m1 * m2
print(m3)

#print(m.max())

