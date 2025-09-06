import numpy as np

# Zeros
ar_zero = np.zeros(4)  # Create 1D array of 4 elements, all zeros
ar_zero1 = np.zeros((3,4)) # Create 2D array (3 rows, 4 columns), all zeros
print(ar_zero)             # Print 1D zero array
print()                    # Print blank line for spacing
print(ar_zero1)            # Print 2D zero array

# Ones
ar_one = np.ones(4)  # Create 1D array of 4 elements, all ones
print(ar_one)

# Empty
ar_em = np.empty(4)  # Create 1D array of size 4 with random garbage values (not initialized)
print(ar_em)

# Range
ar_rn = np.arange(4)       # Create array with values from 0 to 3
print(ar_rn)               # Print the range array

# Diagonal
ar_dia = np.eye(3)        # Create 3x3 identity matrix (diagonal ones, rest zeros)
print(ar_dia)

ar_dia1 = np.eye(3,5)     # Create 3x5 matrix with diagonal ones (rectangular identity form)
print(ar_dia1)

# Linspace
ar_lin = np.linspace(0, 20, num=5)  # Create array with 5 evenly spaced values from 0 to 20
print(ar_lin)
