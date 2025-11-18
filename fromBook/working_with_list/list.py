# chapter 3 
#  introducing lists 

# what is list 
#  def:  A list is a collection of items in a particular order


# //////

# bicycles = ["trek", "cannondale", "redline", "specialized"]
# print(bicycles) # the output return with brackets // ['trek', 'cannondale', 'redline', 'specialized']


# 

# Accessing Elements in a List

# bicycles = ["trek", "cannondale", "redline", "specialized"]
# print(bicycles[0])

# 

# Using Individual Values from a List

# bicycles = ["trek", "cannondale", "redline", "specialized"]
# message = f"My favorite bicycle was a {bicycles[-1].title()}"
# print(message) # My favorite bicycle was a Specialized

# 

# friends = ["karem", "imtiaz", "nasir", "farman"]
# print(friends)
# print(friends[0])

# 

# friends = ["karem", "imtiaz", "nasir", "farman"]
# message = f"they all are my friends we play football together {friends}"    
# print(message)

# 

#  Modifying Elements in a List

# motorcycles = ["honda", "yamaha", "suzuki"]
# print(motorcycles) # ['honda', 'yamaha', 'suzuki']

# motorcycles[0] = 'ducati'
# print(motorcycles) # ['ducati', 'yamaha', 'suzuki']

# 

# motorcycles = ["honda", "yamaha", "suzuki"]
# motorcycles[1] = 'honda'
# print(motorcycles)

# 

#  Appending Elements to the End of a List
# Append is a method who's add elements to the ends of the list 

# motorcycles = ['honda', 'yamaha', 'suzuki']
# motorcycles.append('ducati')
# print(motorcycles)

# 

# motorcycles = []
# motorcycles.append('honda')
# motorcycles.append('yamaha')
# motorcycles.append('suzuki')
# print(motorcycles) #  ['honda', 'yamaha', 'suzuki']

# 

# Inserting Elements into a List
# insert is a methods add elements in any possition 

# motorcycles = ['honda', 'yamaha', 'suzuki']
# motorcycles.insert(2, 'ducati')
# print(motorcycles)

# 

# Removing an Item Using the del Statement

# motorcycles = ["honda", "yamaha", "suzuki"]
# del motorcycles[0]
# print(motorcycles) # ['yamaha', 'suzuki']

# 

# Removing an Item Using the pop() Method

# fruits = ["apple", "banana", "cherry"]
# last = fruits.pop() 
# print(last) # cherry

# 

# motorcycles = ["suzuki", "yamaha", "honda"]
# last_owned = motorcycles.pop() 
# print(f"the last motercycles I owned was a {last_owned}")

# 

# Removing an Item by Value

# motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
# motorcycles.remove("suzuki")
# print(motorcycles)  # ['honda', 'yamaha', 'ducati']

# 

# motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
# to_expensive = "suzuki"
# print(f" A {to_expensive} is too expansive for me"); 
 
# 

#  Sorting a List Permanently with the sort() Method 

# cars = ['bmw', 'audi', 'toyota', 'subaru']
# cars.sort() 
# print(cars)


# 

# cars = ['bmw', 'audi', 'toyota', 'subaru']
# cars.sort(reverse=True)
# print(cars)

# 


# cars = ['bmw', 'audi', 'toyota', 'subaru']
# print(cars)
# print("\n Here is the sorted list:")
# print(sorted(cars))


# 

#  Printing a List in Reverse Order

# cars = ['bmw', 'audi', 'toyota', 'subaru']
# cars.reverse()
# print(cars)

# 

# Finding the Length of a List

# cars = ['bmw', 'audi', 'toyota', 'subaru']
# len(cars)


# 

# Avoiding Index Errors When Working with Lists

# list = ["Honda", "suzuki", "mehran"]
# print(list[4])

# 


# list = []   
# print(list[-1])


# 

# list = ["honda", "toyota", "suzuki"]
# print(len(list)) # 3

# 

# list = ["naib", "ali", "junaid", "zuhan", "zain"]   

# list.sort()
# print(list)

# print(len(list))

# list.sort(reverse=True)
# print(list)


































