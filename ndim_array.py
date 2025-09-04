import numpy as np   # Import numpy library

# ----------- Example 1: 2D Array -----------
ar1 = np.array([[1,2,3,4],[1,2,3,4]])   # Create a 2D array (2 rows, 4 columns)
print(ar1)                              # Print array
print(ar1.ndim)                         # Print number of dimensions (2D → 2)

# ----------- Example 2: 3D Array -----------
ar2 = np.array([[[1,2,3,4],[1,2,3,4],[1,2,3,4]]])  # Create a 3D array (1 block, 3 rows, 4 cols)
print(ar2)                                         # Print array
print(ar2.ndim)                                    # Print number of dimensions (3D → 3)

# ----------- Example 3: Forcing Higher Dimensions -----------
arn = np.array([1,2,3,4], ndmin = 10)  # Force array to have 10 dimensions using 'ndmin'
print(arn)                             # Print array (many nested brackets)
print(arn.ndim)                        # Print number of dimensions (10D → 10)
