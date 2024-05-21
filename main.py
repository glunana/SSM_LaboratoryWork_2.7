import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

x1 = np.linspace(0, 2.5, 400)
x2 = np.linspace(0, 13, 400)
X1, X2 = np.meshgrid(x1, x2)

F1 = X1 - np.cos(X2) - 1
F2 = X2 - np.log(X1 + 1) - 11

plt.contour(X1, X2, F1, levels=[0], colors='r')
plt.contour(X1, X2, F2, levels=[0], colors='b')
plt.xlabel('x1')
plt.ylabel('x2')
plt.grid(True)
plt.show()

def g1(x2):
    return 1 + np.cos(x2)

def g2(x1):
    return 11 + np.log(x1 + 1)

x1, x2 = 1.9, 12
tolerance = 1e-6
max_iterations = 100

for _ in range(max_iterations):
    x1_new = g1(x2)
    x2_new = g2(x1)

    if np.abs(x1_new - x1) < tolerance and np.abs(x2_new - x2) < tolerance:
        break

    x1, x2 = x1_new, x2_new

print(f'Метод простих ітерацій: x1 = {x1:.6f}, x2 = {x2:.6f}')

def equations(vars):
    x1, x2 = vars
    eq1 = x1 - np.cos(x2) - 1
    eq2 = x2 - np.log(x1 + 1) - 11
    return [eq1, eq2]

initial_guess = [1.9, 12]

solution = fsolve(equations, initial_guess)
x1, x2 = solution

print(f'Метод Ньютона: x1 = {x1:.6f}, x2 = {x2:.6f}')