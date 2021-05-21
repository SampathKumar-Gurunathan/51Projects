# -*- coding: utf-8 -*-
"""
Created on Fri May 21 17:50:50 2021

@author: sampathkumar
"""

# Sampath Python Assigment
# setting the Variable
t_Var = "Hello World"
print (t_Var)

# Print the variables memory address
print(id(t_Var))

# Changing the value of the variable
t_Var = "Changed Hello World"
print (t_Var)

# creating a variable
t_Name = "Eric"
# Concatinating two text.
print("Hello "+t_Name+", would you like to learn some Python today?")

# Create a Quote
t_Quote = '"Dream. Dreams do come true."'
print("Sachin once said,"+ t_Quote)

# Create a Variable to store person name
famous_person = "Sachin"
print(famous_person+" once said,"+t_Quote)

# Addition
print(5+3)

# Subtraction
print(11-3)

# Multiplication
print (4*2)

# Division
print(16/2)

# Favorite Number
t_Num = 3
print("My facvorite number is:",t_Num)
print("My favorite number is: {first}".format(first=t_Num))

# List of Name
L_Name = ["Sam","Jay","Rud"]
#Loop through each Name.
i = 0
while i < len(L_Name):
  print(L_Name[i])
  i = i + 1
#Loop through each Name and print with Message.
i = 0
while i < len(L_Name):
  print("Hi "+L_Name[i]+". How are you doing?")
  i = i + 1
  
# Transportaion Variable
L_Trans = ["Bus","Train","Plane"]
#Loop through each Transport and print with Message.
i = 0
while i < len(L_Name):
  if i==0:
    print("I commute to office by "+L_Trans[i]+" Daily.")
  elif i==1:
    print("I visit my parents in my native by "+L_Trans[i]+" monthly.")
  else:
    print("I travel by "+L_Trans[i]+" during official trips.")
  i = i + 1