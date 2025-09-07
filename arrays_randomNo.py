import numpy as np

var = np.random.rand(4)  # Create a 1D array of 4 random numbers between 0 and 1
print(var)

print("\n")

var1 = np.random.rand(2, 5)  # Create a 2D array (2 rows, 5 columns) with random numbers between 0 and 1
print(var1)


var2 = np.random.ranf(4) # Generate a 1D array of 4 random float numbers in range [0, 1)
print(var2)

var3 = np.random.randint(5, 20, 5)  # Generate 5 random integers between 5 (inclusive) and 20 (exclusive)
print(var3)
