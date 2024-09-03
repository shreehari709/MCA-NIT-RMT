import sympy as sp
from sympy import *

#function_input = input("Enter a Objective function function: ")

# Convert the string input into a callable function
x,y,l=sp.symbols('x,y,l')

# Take user inputs
#z_fun = input("Enter the expression for z_fun (in terms of x and y) ex(4*x**2 - 2*x*y + 6*y**2): ")
#constraint = input("Enter the expression for constraint (in terms of x, y, and l)(72*l -x*l-l*y): ")
#gx = float(input("Enter the value for gx: "))
#gy = float(input("Enter the value for gy: "))

# Convert string inputs into sympy expressions
#z_fun = sp.sympify(z_fun_input)
#constraint = sp.sympify(constraint_input)

ob_fun= 4*x**2 - 2*x*y + 6*y**2 + 72*l -x*l-l*y
z_fun = 4*x**2 - 2*x*y + 6*y**2 
constraint = 72*l -x*l-l*y

ob_fun = (z_fun) + (constraint)
 
print("Expression : {}".format(ob_fun))
  
# Use sympy.Derivative() method 
diff_x = sp.diff(ob_fun, x)  
diff_y = sp.diff(ob_fun, y)  
diff_l = sp.diff(ob_fun, l)  
gx=-1
gy=-1     

print("Value of the derivative : {} ".format(diff_x.doit()))
     
 
print("Value of the derivative : {} ".format(diff_y.doit()))

print("Value of the derivative : {} ".format(diff_l.doit()))

solutions = sp.solve([diff_x, diff_y, diff_l], (x, y, l))

# Display the solutions
#print("\nSolutions:")
#for var, value in solutions.items():
#    print(f"{var} = {value}")
        
        
diff_xx = sp.diff(diff_x, x)  

diff_xy = sp.diff(diff_x, y)
 
diff_yx = sp.diff(diff_y, x) 
 
diff_yy = sp.diff(diff_y, y)

determinants=diff_xx*(0-gy*gy)-diff_xy*(0-gy*gx)+gx*(diff_yx*gy - diff_yy*gx)  
print(determinants)

x_sol = solutions[x]
y_sol = solutions[y]
l_sol = solutions[l]

# Display the stored solutions
#print("\nStored Solutions:")
print(f"x = {x_sol}")
print(f"y = {y_sol}")
print(f"λ = {l_sol}")

def zmin(x, y):
    return 4*(x**2) - 2*x*y + 6*y**2

def zmax(x, y):
    return 4*x**2 - 2*x*y + 6*y**2

# Check the determinant to determine if it's a minimum or maximum
if determinants > 0:
    zmax_value = zmax(x_sol, y_sol)
    print("Z max =", zmax_value)
else:
    zmin_value = zmin(x_sol, y_sol)
    print("Z min =", zmin_value)
    