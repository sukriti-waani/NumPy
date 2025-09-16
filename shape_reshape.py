import numpy as np

# Shape
var = np.array([[1,2,3,4],[1,2,3,4]])
print(var)
print()
print(var.shape)

# Correct way to create higher dimension array
var1 = np.array([1,2,3,4])
var1 = np.reshape(var1, (1,1,1,4))   # making it 4D
print(var1)
print(var1.ndim)
print()
print(var1.shape)


#  Reshape
var2 = np.array([1,2,3,4,5,6])
print(var2)
print(var2.ndim)

x = var2.reshape(2,3)
print(x)
print(x.ndim)
