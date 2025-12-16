# Simple idea
# Try to run code
# If an error happens, catch it and handle it

# 
# Example 1(Very easy)

# try: 
#     num = int(input("Enter a number ")) 
#     print(10 / num) 
# except: 
#     print("Something went wrong! ")

# 

# Example 2(More clear & specific)

# try: 
#     num = int(input("Enter a number "))
#     print(10 / num)
# except ZeroDivisionError: 
#     print("You can not divided by zero ") 
# except ValueError: 
#     print("Please enter a valid number ") 


# 

# import math

# a_number = int(input("Please enter an integer: ")) 

# try: 
#     print(math.sqrt(a_number)) 
# except: 
#     print("Bad value for square root") 
#     print("Using absolute value instead") 
#     print(math.sqrt(abs(a_number)))


# 

# Function 

# def square(n): 
#     return n ** 2 
# print(square(5))
# print(square(square(3))) 

# 

def square_root(n): 
    root = n / 2
    for k in range(20): 
        root = (1 / 2) * (root + (n / root))
    return root 

print(square_root(9)) 





    
    
    









