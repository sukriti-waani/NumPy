import numpy as np

x = [1,2,3,4]
y = np.array([1, 2, 3, 4, 5])

print(y)
print(type(y))


l = []
for i in range(1, 5):
  int_l = input("Enter: ")
  l.append(int_l)

print(np.array(l))