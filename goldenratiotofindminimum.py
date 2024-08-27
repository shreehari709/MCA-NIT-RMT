
#Minimizarion of the function using Golden Ratio
def golden_section_search(f, l, r, tol):
    golden_ratio = 0.618  
    iteration = 1
    
    while (r - l) > tol:
        # X2 and  X1 ko meow meow kar do
        #round() function decimal ke baad values ko set kar sakte hai 
        x2 =round(l + golden_ratio*(r - l),3) 
        x1 =round((l+r) - x2,3) 
        # Print the current interval
        print(f"Iteration {iteration}: Interval = [{l}, {r}]")
        
        # Evaluate the function at the interior points
        fx2 = f(x2)
        fx1 = f(x1)
        
        # 
        if fx1 < fx2:
            r = x2
        else:
            l = x1
            
        iteration += 1
    
    # Calculate the mean of the last interval
    final_mean = (l + r) / 2
    
    # Print the last interval and the mean
    print(f"Final Interval: [{l}, {r}]")
    print(f"Mean of the final interval: {final_mean}")
    return final_mean

# User input for the function as a string
function_input = input("Enter a function of x to minimize (e.g., 'x**2 '): ")

# Convert the string input into a callable function
f = eval(f"lambda x: {function_input}")

# User input for the interval [a, b]
l_input = input("Enter the Lower Bound of the interval (l): ")
r_input = input("Enter the Upper Bound of the interval (r): ")

# Convert the inputs 
l = int(l_input)
r = int(r_input)

# Stopping tolerance diya hua aagar ye 
tol = 0.13

# Function ko call kar rahe hai yahan 
golden_section_search(f, l, r, tol)
