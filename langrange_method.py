import sympy as sp

# Define symbols
x, y, l = sp.symbols('x y l')

# Take user inputs
z_fun_input = input("Enter the expression for z_fun (in terms of x and y): ")
constraint_input = input("Enter the expression for constraint (in terms of x, y, and l): ")
gx = float(input("Enter the value for gx: "))
gy = float(input("Enter the value for gy: "))

# Convert string inputs into sympy expressions
z_fun = sp.sympify(z_fun_input)
constraint = sp.sympify(constraint_input)

# Objective function
ob_fun = z_fun + constraint
print("Expression : {}".format(ob_fun))

# Compute derivatives
diff_x = sp.diff(ob_fun, x)
diff_y = sp.diff(ob_fun, y)
diff_l = sp.diff(ob_fun, l)

print("Value of the derivative with respect to x: {} ".format(diff_x.doit()))
print("Value of the derivative with respect to y: {} ".format(diff_y.doit()))
print("Value of the derivative with respect to λ: {} ".format(diff_l.doit()))

# Solve the system of equations
solutions = sp.solve([diff_x, diff_y, diff_l], (x, y, l))

# Check if solutions exist
if solutions:
    # If solutions is a list of dictionaries, extract the first solution
    if isinstance(solutions, dict):
        solution = solutions
    else:
        solution = solutions[0]

    x_sol = solution[x]
    y_sol = solution[y]
    l_sol = solution[l]

    print(f"x = {x_sol}")
    print(f"y = {y_sol}")
    print(f"λ = {l_sol}")

    # Compute second derivatives for determinant calculation
    diff_xx = sp.diff(diff_x, x)
    diff_xy = sp.diff(diff_x, y)
    diff_yx = sp.diff(diff_y, x)
    diff_yy = sp.diff(diff_y, y)

    # Compute the determinant
    determinants = (diff_xx * (0 - gy * gy) - 
                    diff_xy * (0 - gy * gx) + 
                    gx * (diff_yx * gy - diff_yy * gx))
    
    print("Determinant: ", determinants)

    # Define the functions for zmin and zmax
    def zmin(x_val, y_val):
        return z_fun.subs({'x': x_val, 'y': y_val})

    def zmax(x_val, y_val):
        return z_fun.subs({'x': x_val, 'y': y_val})

    # Check the determinant to determine if it's a minimum or maximum
    if determinants > 0:
        zmax_value = zmax(x_sol, y_sol)
        print("Z max =", zmax_value)
    else:
        zmin_value = zmin(x_sol, y_sol)
        print("Z min =", zmin_value)
else:
    print("No solutions found.")
