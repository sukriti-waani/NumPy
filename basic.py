import numpy as np

# Create numpy array
x = np.array([1, 2, 3, 4])
print(x)
print(type(x))   # <class 'numpy.ndarray'>

# Create normal Python list
y = [1, 2, 3, 4]
print(y)
print(type(y))   # <class 'list'>


import time

start = time.time()
result = [j**4 for j in range(1, 9)]
end = time.time()

print("Result:", result)
print("Execution time:", end - start, "seconds")
