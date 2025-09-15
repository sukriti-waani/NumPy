import numpy as np

# Add 3 to each element
var = np.array([1, 2, 3, 4])
# varadd = var + 3
varadd = np.add(var,3)
print(varadd)

print("\n")

# Add two arrays element-wise
var1 = np.array([1, 2, 3, 4])
var2 = np.array([1, 2, 3, 4])
# varadd1 = var1 + var2
varadd1 = np.add(var1, var2)
print(varadd1)

# Multiply each element by 3
var = np.array([1, 2, 3, 4])
varadd2 = var * 3
print(varadd2)

print("\n")

# Divide each element by 3
var2 = np.array([1, 2, 3, 4])
varadd3 = var2 / 3
print(varadd3)

print("\n")

var2 = np.array([1, 2, 3, 4])
varadd3 = var2 % 3
print(varadd3)

print("\n")

var3 = np.array([1,2,3,4])
varadd = np.reciprocal(var)
print(varadd)

print("\n")

# 2D Array
var21 = np.array([[1,2,3,4],[1,2,3,4]])
var22 = np.array([[1,2,3,4],[1,2,3,4]])

print(var21)
print()
print(var22)
print()

varadd2 = var21 + var22
print(varadd2)