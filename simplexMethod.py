import numpy as np
from scipy.optimize import linprog

def main():
    # Get the number of variables
    num_vars = int(input("Enter the number of variables: "))

    # Get coefficients of the objective function
    print("Enter the coefficients of the objective function (space-separated):")
    c = list(map(float, input().split()))
    c = [-coef for coef in c]  # Negate for minimization (since linprog minimizes by default)

    # Get the number of constraints
    num_constraints = int(input("Enter the number of constraints: "))

    A = []
    b = []

    # Input each constraint
    for i in range(num_constraints):
        print(f"Enter the coefficients for constraint {i + 1} (space-separated):")
        constraint = list(map(float, input().split()))
        A.append(constraint)

        print(f"Enter the right-hand side value for constraint {i + 1}:")
        rhs = float(input())
        b.append(rhs)

    # Get variable bounds
    bounds = []
    for i in range(num_vars):
        print(f"Enter the bounds for variable x{i + 1} (min max, space-separated, or just hit enter for [0, None]):")
        bounds_input = input()
        if bounds_input:
            bounds.append(tuple(map(float, bounds_input.split())))
        else:
            bounds.append((0, None))  # Default non-negativity

    # Run the Simplex method
    result = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')

    # Display the results
    if result.success:
        print(f"Optimal value: {-result.fun}")  # Negate again to get the max value
        for i in range(num_vars):
            print(f"x{i + 1}: {result.x[i]}")
    else:
        print("No solution found.")

# Fix the name check block
if __name__ == "__main__":
    main()
