# NUMPY:
import numpy as np
# Create arrays
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
# Element-wise addition
c = a + b
print("Array Addition:", c)
# Matrix multiplication
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
product = np.dot(A, B)
print("Matrix Multiplication:\n", product)
# MATPLOTLIB:
import matplotlib.pyplot as plt
# Line plot
x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y)
plt.title("Sine Wave")
plt.xlabel("x-axis")
plt.ylabel("sin(x)")
plt.grid(True)
plt.show()
# PANDAS:
import pandas as pd
# Create DataFrame
data = {'Name': [' Gunveer Singh', 'Rohit', 'Sumit'],
 'Marks': [85, 90, 95]}
df = pd.DataFrame(data)
print("DataFrame:\n", df)
# Basic stats
print("\nAverage Marks:", df['Marks'].mean())
