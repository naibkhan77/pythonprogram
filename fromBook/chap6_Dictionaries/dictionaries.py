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



# alien_0 = {'color': 'green', 'point': 5, 'speed': 'slow'} 
# del alien_0['speed']
# print(alien_0)


# 


# A Dictionary of Similar Objects

# favorite_languages = {    
#     'jen': 'javaScript', 
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

# user_0 = {
#     'username': 'khan', 
#     'first': 'Muhammad', 
#     'last': 'naib',
# }

# for key, value in user_0.items(): 
#     print(f"\nKey: {key}")
#     print(f"\nValue {value}:")
    

# 


# favorite_language = {
#     'jen': 'python', 
#     'sara': 'c', 
#     'edward': 'rust', 
#     'phil': 'javaScript'
# }

# for name in favorite_language.keys(): 
#     print(name.title()) 

# for name in favorite_language: 
#     print(name)
    
    
# 


# favorite_language = {
#     'jen': 'python', 
#     'zain': 'c', 
#     'edward': 'rust', 
#     'phil': 'javaScript'
# }

# friends = ['phil', 'sarah']
# for name in favorite_language.keys(): 
#     print(f"Hi {name}. ")
    
#     if name in friends: 
#         language = favorite_language[name]
#         print(f"\n{name.title()}, I see you love {language}")
        
        
# 

# Looping Through a Dictionary’s Keys in a Particular Order


# favorite_language = {
#     'jen': 'js', 
#     'zain': 'c', 
#     'edward': 'rust', 
#     'phil': 'python', 
# }

# for name in sorted(favorite_language.keys()): 
#     print(f"{name.title()}, thank you for taking the poll, ") 
    

#

# Looping Through All Values in a Dictionary

# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'rust',
#     'phil': 'js',
# }

# print("The following language have been mentioned: ") 

# for language in favorite_languages.values(): 
#     print(language.title()) 
    

# 

# Set() removes duplicates and returns unique values only.

# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'rust',
#     'phil': 'js',
# }

# print("The following language have been mentioned: ") 
# for language in set(favorite_languages.values()): 
#     print(language.title())


# 

# Nesting 

#  A list of Dictionaries 

# alien_0 = {'color': 'green', 'points': 5}
# alien_1 = {'color': 'yellow', 'points': 10} 
# alien_2 = {'color': 'red', 'points': 15}

# aliens = [alien_0, alien_1, alien_2] 

# for alien in aliens: 
#     print(alien)


# 

# make an empty list for storing aliens.

# aliens = [] 

# # Make 30 green aliens. 

# for _ in range(15): 
#     new_alien = {'color': 'green', 'point': 5, 'speed': 'slow'}
#     aliens.append(new_alien)
    
# # Show the first 5 aliens. 

# for alien in aliens[:3]: 
#     print(alien)
#     print("...")

# # Show how many aliens have been created. 
# print(f"Total number of aliens: {len(aliens)}")

# 


# aliens = [] 

# for _ in range(30): 
#     new_alien = {'color': 'green', 'point': 5, 'speed': 'slow'}
#     aliens.append(new_alien)    
    
# for alien in aliens[:3]:
#     if alien['color'] == 'green': 
#         alien['color'] = 'yellow'
#         alien['speed'] =  'medium'
#         alien['point'] = 10
        
# for alien in aliens[:5]: 
#     print(alien)
# print("...")


# 

# pizza = {
#     'crust': 'think', 
#     'toppings': ['mushrooms', 'extra cheese'], 
# }

# # Summarize the order. 

# print(f"You ordered a {pizza['crust']}-crust pizza " "with the following toppings:")

# for topping in pizza['toppings']: 
#     print(f"\n{topping}")
    

# 


# favorite_language = {
#     'jen': ['python', 'rust'], 
#     'sara': ['c'], 
#     'edward': ['rust', 'go'], 
#     'phil': ['python', 'haskell'], 
# }

# for name, languages in favorite_language.items(): 
#     print(f"\n{name.title()}'s favorite languages are: ")
#     for language in languages: 
#         print(f"\t{language.title()}")


# 

# A Dictionary in a Dictionary

# users = {
#     'Alice': {
#         'first': 'john', 
#         'last': 'wood', 
#         'location': 'islamabad',
#     }, 
    
#     'zain': {
#         'first': 'khan', 
#         'last': 'zubir', 
#         'location': 'paris', 
#     }, 
# }

# print(users['Alice'])

# for username, user_info in users.items(): 
#     print(f"\nUsername: {username}")
#     full_name = f"{user_info['first']} {user_info['last']}"
#     location = user_info['location']
    
#     print(f"\tFull name: {full_name.title()}")
#     print(f"\tLocation: {location.title()}")

# 


#  TRY IT YOURSELF 

# 6-8. Pets: Make several dictionaries, where each dictionary represents a differ
# ent pet. In each dictionary, include the kind of animal and the owner’s name. 
# Store these dictionaries in a list called pets. Next, loop through your list and as 
# you do, print everything you know about each pet.


# pet1 = {'animal': 'dog', 'owner': 'jim'}
# pet2 = {'animal': 'cat', 'owner': 'alice'}  
# pet3 = {'animal': 'pinguines', 'owner': 'sara'}

# pets = [pet1, pet2, pet3] 

# for pet in pets: 
#     print("\nPet Information")
#     for key, value in pet.items(): 
#         print(f"{key} {value}")

# 
        
# animals = {
#     'pit1': {'animal': 'god', 'owner': 'zain'},
#     'pit2': {'animal': 'cat', 'owner': 'alice'},
#     'pit3': {'animal': 'lion', 'owner': 'sara'}
# }

# for name, animal_info in animals.items():
#     print(f"\n{name}'s information: ")
#     for key, value in animal_info.items(): 
#         print(f"\t{key.title()}: {value}")
    


# 

#  Favorite Places: Make a dictionary called favorite_places. Think of three 
# names to use as keys in the dictionary, and store one to three favorite places for 
# each person. To make this exercise a bit more interesting, ask some friends to 
# name a few of their favorite places. Loop through the dictionary, and print each 
# person’s name and their favorite places.


favorite_places = {
    'sara': ['tokyo', 'paris', 'dubai'], 
    'alice': ['new york', 'rome'], 
    'john': ['london']
}

for name, places in favorite_places.items(): 
    print(f"\n{name}  favorite place are: ") 
    for place in places: 
        print(f"\t-{place}")

    
    
    
    


    
    



 










        
    
    




































