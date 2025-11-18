# In Python, a dictionary is a collection of key-value pairs.
# It’s used to store data where each value is accessed using its key.


# 

# alien_0 = {'color': 'green', 'point': 109} 

# print(alien_0['color'])


# 

# Accessing Values in a Dictionary

# alien_0 = {'color': 'green'} 
# print(alien_0['color'])


# 

# alien_0 =  {'color': 'green', 'points': 10}

# new_point = alien_0['points'] 
# print(f"You just earned {new_point} points!")


# 

# alien_0 = {'color': 'blue', 'point': 10} 

# new_color = alien_0['color']
# print(f"Your color is {new_color} color :")


# 

# alien_0 = {'color': 'green', 'points': 6} 
# print(alien_0) 


# alien_0['x_position'] = 0 
# alien_0['y_position'] = 25
# print(alien_0) 


# 


# Starting with an Empty Dictionary

# alien_0 = {} 

# alien_0['color'] = 'blue'
# alien_0['point'] = 9

# print(alien_0)  


# 

# Modifying values in a Dictionary 

# alien_0 = {'color': 'green'} 
# print(f"The aligen is {alien_0['color']}.")


# alien_0['color'] = 'yellow'
# print(f"The align is now {alien_0['color']}.") 


# alien_0['color'] = "blue" 
# print(f"The alien is now {alien_0['color']}.") 


# 


# alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
# print(f"Original position: {alien_0['x_position']}")

# # Move to align to the right 
# if alien_0['speed'] == 'slow': 
#     x_increment = 1
# elif alien_0['speed'] == 'medium':
#     x_increment = 2
# else: 
#     x_increment = 3
    
# alien_0['x_position'] += x_increment

# print(f"New positon: {alien_0['x_position']}")


#  Removing Key-Value Pairs

# alien_0 = {'color': 'green', 'points': 5}   
# del alien_0['points']

# print(alien_0) # delete the point key values # output just ('color' 'green)


# 


# A Dictionary of Similar Objects

# favorite_languages = {    
#     'jen': 'python', 
#     'sarah': 'c', 
#     'edward': 'rust', 
#     'naib': 'python',    
# }

# language = favorite_languages['naib'].title()
# print(f"Naib favoite language is {language} .")



# 

# .get() is a safe way to access a key in a dictionary.

# alien_0 = {'color': 'green', 'speed': 'slow'}

# point_value = alien_0.get('points', 'No point value assigned.')
# print(point_value)


#  TRY IT YOURSELF 

#  Person: Use a dictionary to store information about a person you know. 
# Store their first name, last name, age, and the city in which they live. You 
# should have keys such as first_name, last_name, age, and city. Print each piece  
# of information stored in your dictionary.


# person = {'first_name': 'Muhammad', 'last_name': 'Naib', 'age': 25, 'city:': 'Peshawer'}

# dictionary = person['first_name']

# print(f"{person['first_name']} {person['last_name']} is {person['age']} year old and live in {person['city:']}")



# 

#  Favorite Numbers: Use a dictionary to store people’s favorite numbers. 
# Think of five names, and use them as keys in your dictionary. Think of a favorite 

# favorite_Number = {
#     'Alice': 7, 
#     'John': 3, 
#     'Zain': 10, 
#     'David': 8, 
#     'Emma': 1   
# }

# print(f"Alice favorite number is : {favorite_Number['Alice']}")
# print(f"Zain favotire no is {favorite_Number['Zain']}")  # and so on 


# 


# Looping Through a Dictionary






































