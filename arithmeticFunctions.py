import numpy as np

# 1D numpy array
var = np.array([1,2,3,4,5,3,2])

# Print minimum value and its index (argmin gives index of first min value)
print("min : ", np.min(var), np.argmin(var))

# Print maximum value and its index (argmax gives index of first max value)
print("max : ", np.max(var), np.argmax(var))

# Print square root of each element in the array
print("Sqrt : ", np.sqrt(var))

print("\n")

# 2D numpy array
var1 = np.array([[2,1,3],[9,5,6]])

# Find min values column-wise (axis=0 → compare elements vertically)
print(np.min(var1, axis=0))

print("\n")


var2 = np.array([1,2,3])

# Print sine of each element (in radians)
print(np.sin(var2))

# Print cosine of each element (in radians)
print(np.cos(var2))

# Print cumulative sum → adds elements one by one (1, 1+2, 1+2+3)
print(np.cumsum(var2))
