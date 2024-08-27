def fibonacci_search(f, l, r, n):
    # Calculate Fibonacci series up to n terms
    
    fib = [1, 1]
    while len(fib) <= n:
        fib.append(fib[-1] + fib[-2])
    
    k = 1
    while k < n:
        # Calculate the ratio of the Fibonacci numbers
        fk = (fib[n] - k)/( fib[n-k+1])
        ratio = round(fk, 3)
        # x1 = d , x2 = c
        x2 = round(l + ratio * (r - l), 3)
        x1 = round((l + r) - x2, 3)
        
        # Evaluate the function at c and d
        fx2 = f(x2)
        fx1 = f(x1)
        
        # Print the current interval
        print(f"Iteration {k}: Interval = [{l}, {r}]")
        
        # Narrow the interval based on the function evaluations
        if fx2 > fx1:
            r = x2
        else:
            l = x1
        
        k += 1
    
    # Calculate the mean of the last interval
    final_mean = (l + r) / 2
    
    # Print the final interval and mean
    print(f"Final Interval: [{l}, {r}]")
    print(f"Mean of the final interval: {final_mean}")
    return final_mean

# User input for the function
function_input = input("Enter a function of x to minimize (e.g., 'x**2'): ")

# Convert the string input into a callable function
f = eval(f"lambda x: {function_input}")

# User input for the interval [l, r]
l_input = input("Enter Lower Bound of the interval (l): ")
r_input = input("Enter Upper Bound of the interval (r): ")

# Convert the inputs to integers
l = int(l_input)
r = int(r_input)

# User input for the number of iterations (n)
n = int(input("Enter the number of iterations (n): "))

# Perform the Fibonacci Search
fibonacci_search(f, l, r, n)
