# chapter 5 if Statement

#  there are two membreship operator in python (in , not in) 

# cars = ['audi', 'bmw', 'subara', 'toyota']

# for car in cars: 
#     if car == 'bmw':
#         print(car.upper())
#     else: 
#         print(car.title())
        
# 

# cars = ['audi', 'bmw', 'subara', 'toyota']

# for car in cars: 
#     if car == 'audi' or car == 'bmw':
#         print(car.upper())
#     else: 
#         print(car.title())  
        
# 

# Ignoring Case When Checking for Equality

# False 

# car = "Audi" 
# car == 'audi' 

# 

# True

# car = 'Audi' 
# car.lower() == 'audi'

# print(car)


# 

# Checking for Inequality // inequality operator (!=). 

# requested_topping = 'mashrooms' 

# if requested_topping != 'anchvies':
#     print('Hello the anchovies!')

# 

# Numerical Comparisons

# True 

# age = 18 
# age == 18 


# age = 17 
# if age != 24: 
#     print("that is not the correct answer. Please try again!")
    
# 

# Using and to Check Multiple Conditions

# age_0 = 22 
# age_1 = 18 
# result = age_0 >= 21 and age_1 >= 21
# print(result) # false 


# 

# age_0 = 22
# age_1 = 18
# result = age_0 >= 21 or age_1 >= 21 
# print(result) # true 

# 

# Checking Whether a Value Is in a List

# requesting_toppings = ['mashrooms', 'onions', 'pineapple']
# result = 'onions' in requesting_toppings
# print(result)

# 

# Checking Whether a Value Is Not in a List

# banned_users = ['alice', 'maxwell', 'root', 'kholi']
# user = 'baber'
# if user not in banned_users: 
#    print(user) 
    
    
    
#//////////////   Boolean Expressions ///////////////

# if and if-else statement 


# age = 19 
# if age > 18: 
#    print("You are old enough to vote!"); 
   

# 

# age = 17
# if age >= 18: 
#    print("You are old engough to vote!") 
# else: 
#    print("Sorry, you are too young to vote.") 
   

# 


#  The if-elif-else Chain

# age = 4
# if age <= 4: 
#    print("Your admission cost is $0.")
# elif age < 18: 
#    print("You admission cost is $25.") 
# else: 
#    print("You admission cost is $40.")


# 

# age = 17
# if age < 4: 
#    price = "price is", 0
# elif age < 18: 
#    price = "price is:", 25
# else: 
#    price = "price is:", 40 
# print(f"You admission cost ${price}.")

# 

#  Using Multiple elif Blocks

# age = 61
# if age < 5: 
#    price = 0 
# elif age < 18: 
#    price = 25
# elif age < 60: 
#    price = 40
# else: 
#    price = 20
   
# print(f"You admission cost is ${price}")


# 

#   Testing Multiple Conditions

# requested_toppings = ['mushrooms', 'extra cheese']

# if 'mushrooms' in requested_toppings: 
#    print("Adding mushrooms")
# if 'pepperoni' in requested_toppings: 
#    print("Adding pepperoni")
# if 'extra cheese' in requested_toppings: 
#    print("Adding extera cheese")
# print("\n Finished making you pizza")


### 

# requested_toppings = ['mushrooms', 'extra cheese']

# if 'mushrooms' in requested_toppings:
#    print("Adding mushrooms")
# elif 'pepperoni' in requested_toppings: 
#    print("Adding pepproni")
# elif 'extra cheese' in requested_toppings: 
#    print("Adding extra cheese")
# print("\nFinished making your pizza!")
 
 
#///

# if Statements with Lists

# requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

# for list1 in requested_toppings: 
#    print(f"Adding {list1}.")
# print("/nFinished making your pizza")


#

# requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

# for list1 in requested_toppings: 
#    if list1 == 'green peppers': 
#       print("Yes green peppers are available") 
#    else: 
#       print(f"Adding {list1}")
# print('/n Finished making your pizza!')
   
   
# /////////

# Checking That a List Is Not Empty

# requested_toppings = []

# if requested_toppings: 
#    for list2 in requested_toppings: 
#       print(f"Adding {list2}")
#    print("/n Finished making you pizza!") 
# else:
#    print("Are you sure you want a plain pizza")


# 


#  Using Multiple Lists

   

      
















    
    
    
    
    




        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        