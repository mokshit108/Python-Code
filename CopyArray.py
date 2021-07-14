from numpy import *
'''arr1 = array([1,2,3,4,5])
arr1 = arr1 + 5
print(arr1)
arr2 = array([1,2,3,4,5])
arr3 = array([6,7,8,9,105])
print(concatenate([arr1,arr2])
arr4 = arr2 +arr3 #Vetororized operation
print(arr4)


arr1 = array([25,9,100,4,125])
print(sort(arr1))
'''
'''
arr2 = array([1,2,3,4,5])
arr3 = array([6,7,8,9,105])
print(concatenate([arr2,arr3]))
'''
#Copying

arr1 = array([1,2,3,4,5])
arr2 =  arr1.view()# Deep copy use copy() instead of view()
print(arr1)
print(arr2)
print(id(arr1))
print(id(arr2))

#Shallow copy
#Deep copy