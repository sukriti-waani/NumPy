import numpy as np

var = np.array([1,2,3,12,45,67,16])
print("Data Type : ", var.dtype)

var = np.array([1,0,1.2,1.3])
print("Data Type : ", var.dtype)

var = np.array(["a", "S", "D", "W"])
print("Data Type : ", var.dtype)

var = np.array(["a", "S", "D", "W", 1, 2, 3, 4])
print("Data Type : ", var.dtype)


# Create array with int8 data type (small integer range: -128 to 127)
x = np.array([1,2,3,4], dtype = np.int8)
print("Data Type : ", x.dtype)  # Prints int8
print(x)

# Create array with float data type (using shorthand "f")
x1 = np.array([1,2,3,4], dtype = "f")
print("Data Type : ", x1.dtype)  # Prints float32 (default float type)
print(x1)

# Same float array again
x1 = np.array([1,2,3,4], dtype = "f")
print("Data Type : ", x1.dtype)
print(x1)

print("\n")

# Normal integer array
x2 = np.array([1,2,3,4])

# Convert array x2 into float32
new = np.float32(x2)

# Convert float array back into integer (default int type)
new_one = np.int_(new)

print("Data Type : ", x2.dtype)      # int32 (default int type)
print("Data Type : ", new.dtype)     # float32
print("Data Type : ", new_one.dtype) # int32

print(x2)       # Original int array
print(new)      # Converted to float
print(new_one)  # Converted back to int

print("\n")

# Another integer array
x3 = np.array([1,2,3,4])

# Convert array into float using astype()
new_1 = x3.astype(float)

print(x3)       # Original int array
print(new_1)    # Converted float array
