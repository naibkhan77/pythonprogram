
# print("Algorithms and Data Structures")

# 

# print(2+3*4) #14
# print((2+3)*4) #20
# print(2**10) #1024
# print(6/3) #2.0
# print(7/3) #2.33333333333
# print(7//3) #2
# print(7%3) #1
# print(3/6) #0.5
# print(10//20) #0
# print(3%6) #3
# print(2**100) # 126765060022822940149670320537
# print(5 == 10)  # false 
# print(10 > 5) # true

# //////

# print((5 >= 1) and (5 <= 10)) # True

# the_sum = 0 
# print(the_sum)

# the_sum = 0 
# the_sum = the_sum + 1

# print(the_sum)

# the_sum = 0
# the_sum = True
# print(the_sum)  # True

# /////

# my_word = [0] * 6
# print(my_list)

# my_list = [1, 2, 3, 4]
# A = [my_list] * 4
# print(A)
# my_list [2] = 45
# print(A)

# my_list = [1024, 3, True, 6.5]
# my_list.append(False)
# print(my_list)
# my_list.insert(2, 4.5)  
# print(my_list)


# //////////

#  Trure = True 

# False = False 

#  False or Ture = True 

# Not (False or True) = False 

# True and True = True 

# print ((5 >= 1) and (5 <= 10)) # True 

# the_sum = 0 

# print(the_sum) 

#

# my_list = [1, 2, True, 5.45]
# print(my_list)
 
 
# ////


# my_list = [1, 2, 3, 4] 
# A = my_list * 3
# print(A)


# ////

# my_list = [1024, 3, True, 6.5] 
# my_list.append("niab") # Adds a new item to the end of a list
# print(my_list)

# my_list.insert(1, 6.4) #  Inserts an item at the ith position in a list
# print(my_list)

# print(my_list.pop()) # Removes and returns the last item in a list
# print(my_list)

# print(my_list.pop(1))
# print(my_list)

# my_list.sort() # Modifies a list to be sorted
# print(my_list)

# my_list.reverse() # Modifies a list to be in reverse order
# print(my_list)  

# print(my_list.count(6.5)) #  Returns the number of occurrences of item

# print(my_list.index(6.5)) # Returns the index of the first occurrence of item

# my_list.remove(6.5)

# print(my_list)

# del my_list[0] # Deletes the item in the ith position
# print(my_list)


# ////

# my_list2 = (54). __add__(21)

# print(my_list2)


# 

# range(10) 
# range(0, 10) 
# print(list(range(10))) 

# 

# range(5, 10) 
# print(list(range(5, 10)))

# 

# my_name = "David" 

# # print(my_name * 2) 
# # print(len(my_name))

# A = my_name.upper() 
# print(A)

# A = my_name.center(10) 
# print(A) 

# F = my_name.find("v") 
# print(F)

# F = my_name.split('v') 
# print(F)


#////////

# Strings → immutable 
# Lists → mutable 

# my_list = [1, 4, True, 6.4] 

# my_list[0] = 2**10 

# print(my_list) 

# 

# my_name = "David" 
# my_name[0] = "X"

# print(my_name)  # Error 

# # In this why you mute the string 

# my_name = "David" 
# my_name = "X" + my_name[1:]

# print(my_name)  


# //////

# my_tuple  = (2, True, 4.96)
# print(my_tuple) 

# L = len(my_tuple) 
# print(L) # len 3

# A = my_tuple[0]
# print(A)  # 2

# M = my_tuple * 3
# print(M) 

# A = my_tuple[0:2] 
# print(A) 


# ////

# my_set = (3, 6, "cat", 4.5, False) 

# A = False in my_set 

# print(A)  # True 

# D = 'dog' in my_set  

# print(D) # False


# /////

# union, intersection, issubset, and difference 

# my_set = {False, 3, 4.5, 6, "cat"} 
# your_set = {99, 3, 100} 

# All = my_set.union(your_set) #  Returns a new set with all elements from both sets
# print(All)

# All = my_set.intersection(your_set) # Returns a new set with only the elements common to both sets
# print(All)

# All = my_set & your_set  
# print(All)

# All = my_set.difference(your_set) # Returns a new set with all items from first set not in second
# print(All)

# All = my_set - your_set 
# print(All) 

# All = {3, 100}.issubset(your_set) # Asks whether all elements of one set are in the other
# print(All)

# my_set.add("house")
# print(my_set)

# my_set.pop() 
# print(my_set)   

# my_set.clear() 
# print(my_set)


# ////

# Key value

# capitals = {"Iowa": "DesMoines", "Wisconsin": "Madison"} 
# print(capitals)

# print(capitals["Iowa"])

# capitals["Utah"] = "saltLakeCity" 
# print(capitals)

# print(len(capitals))

# for k in capitals: 
#     print(capitals[k], "is the capital of ", k) 
# print(k)


# 

# phone_ext = {'David': 1401, 'brad': 1137} 

# print(phone_ext.keys()) # ['David', 'brad']
# print(phone_ext.values()) # [1401, 1137]

# print(list(phone_ext.keys()))

# B = "brad" in phone_ext     
# print(B) # True 

# number = 1127 in phone_ext 
# print(number) # False 

# print(phone_ext.items()) 

# print(phone_ext.get("kent", "No Entry")) 


# /////////////

# input and output 

# user_name = input("Please enter your name: ") 

# print("Your name in all capitals is ", user_name.upper(), 
#         "and has length", len(user_name))

# 

# user_radius = input("Please enter the radius of the cricle ") 
# radius = float(user_radius)
# diameter = 2 * radius 


# ////////////

# String formating

# print("Hello world") 

# print("Hello", "World", sep="***") 

# print("Hello", "World", end="***") 

# 

# print(name, "is", age, "year old.")

# print("%s is %d year old." % (name, age)) 


# //////
# %s specifies a string, 
#  %d specifies an integer

# price = 24
# item = "banana" 

# print("The %s costs %d cents" %(item, price)) 
# print(`the ${item} costs ${price} cents`) # same resutl 

# print("The %+10s costs %1.2f cents"% (item, price)) 
# print("The %10s costs %10.3f cents"% (item, price)) 

# 

# item_dict = {"item": "banana", "cost": 24}
# print("The %(item)s cost %(cost)7.1f cents"% item_dict) 



#//////////////

#  Control Structures 

# counter = 1 

# while counter < 5: 
#     print("Hello, world")
#     counter = counter + 1 
    
    
    
# //////


# for item in [1, 2, 3, 4, 5]:  
#     print(item) 
    

# 

# for item in range(5): 
#     # print(item)
#     print(item ** 2)


# 

# loop over each word then loop over each letter 

# word_list = ["cat", "dog", "rabbit"] 
# letter_list = [] 

# for a_word in word_list: 
#     letter_list = [] 
#     for a_letter in a_word: 
#         letter_list.append(a_letter)
#     print(letter_list)
    
# Same things in one line 

# word_list = ["cat", "dog", "rabbit"] 

# letter_list = [letter for word in word_list for letter in word] 
# print(letter_list) 


#

# loops over each word, but does not loop over letters   

# word_list = ['cat', 'dog', 'rabbit']    

# for a_word in word_list: 
#     print(a_word)



# ////

# if n < 0: 
#     print("Sorry, Value is negative") 
# else: 
#     print(math.sqrt(n)) 


# 

# score = 75

# if score >= 90: 
#     print("A") 
# else: 
#     if score >= 80: 
#         print("B")
#     else: 
#         if score >= 70: 
#             print("c") 
#         else: 
#             if score  >= 60: 
#                 print("D") 
#             else: 
#                 print("F") 


# /////


# sq_list = [] 

# for x in range(1, 11): 
#     sq_list.append(x * x) 
# print(sq_list) 

# 

# we can do this in one step 

# sq_list = [x * x for x in range (1,11)]
# print(sq_list) 

# sq_list = [x * x for x in range (1, 11) if x % 2 != 0] 
# print(sq_list) 

# 

# word = "Pakistan"

# for a in word: 
#     if a not in "aeiou": 
#         print(a, end="")



#/////// 



 










    
    



 























































 



