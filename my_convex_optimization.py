import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import linprog


def print_a_function(f, values):
    # Creating vectors X and Y
    x = values
    y = []
    for i in x:
        y.append(f(i))

    fig = plt.figure(figsize = (10, 5))
    # Create the plot
    plt.plot(x, y)
    
    #Saving a picture
    plt.savefig("Plot1.jpg")
    
    # Show the plot
    plt.show()


f = lambda x : (x - 1) ** 4 + x ** 2
values = [1,2,3]
print_a_function(f, values)
print("1/ def print a function")
print("Look at the new generated doc called Plot.jpg")
print()

def find_root_bisection(f, a, b):
    ans = 0
    c = a
    while (b - a) >= 0.001:
        # Find middle point
        c = (a + b) / 2

        # Check if middle point is root
        if (f(c) == 0.0):
            break
        
        # Decide the side to repeat the steps
        if f(c) * f(a) < 0:
            b = c
        else:
            a = c
    return c

f = lambda x : (x - 1) ** 4 + x ** 2
x = find_root_bisection(f, 0, 4)
print("2/ def find root bisection")
print("x value:", "{0:.2f}".format(x))
print()


def find_root_newton_raphson(f, f_deriv, a):
    ite = 0
    h = f(a) / f_deriv(a)
    while abs(h) >= 0.001 and ite < 50:
        h = f(a) / f_deriv(a) 
        a = a - h
        ite += 1
    return a


f = lambda x : (x - 1) ** 4 + x ** 2
f_deriv = lambda x : 4*((x-1)**3) + 2*x
a = 0.4


ans = find_root_newton_raphson(f, f_deriv, a)
print("3/ def find root newton raphson")
print("x value:", "{0:.2f}".format(ans))
print()


def gradient_descent(f, f_prime, start, learning_rate):
    pn_plus_1 = start - learning_rate * f_prime(start)

    while pn_plus_1 < 0.41:
        pn_plus_1 = start - learning_rate * f_prime(start)
        # first iteration after start
        start = pn_plus_1
        pn_plus_1 = start - learning_rate * f_prime(start)

    return start

f = lambda x : (x - 1) ** 4 + x ** 2
f_prime = lambda x : 4*((x-1)**3) + 2*x
start = -1
learning_rate = 0.01

x_min = gradient_descent(f, f_prime, start, learning_rate)
print("4/ def gradient descent")
print("x value:", "{0:.2f}".format(x_min))
print()


def solve_linear_problem(A, b, c):
    # define the upper bound and the lower bound
    x = (0, None)
    y = (0, None)
    res = linprog(c, A_ub=A, b_ub=b, bounds=[x, y])
    
    return round(res.fun), res.x

A = np.array([[2,1],[-4,5],[1,-2]])
b = np.array([10,8,3])
c = np.array([-1,-2])

y, x = solve_linear_problem(A, b, c)

print("5/ def solve linear problem")
print("y value:", y)
print("x value:", x)