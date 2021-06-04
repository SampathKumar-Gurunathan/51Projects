# -*- coding: utf-8 -*-
"""
Created on Sat May 29 12:01:10 2021

@author: sampathkumar
"""
# Assignment 2 for Python

# If Exercise
# 1. Odd or Even
user_input = int(input("Enter an integer: "))
reminder = user_input%2
if reminder == 0:
    print("The entered number is even.")
else:
    print("The entered number is odd.")

# 2. Dog Years to Human Years
dog_years = int(input("Enter the dog years: "))
if dog_years <= 0 or dog_years > 16:
    print("Enter a valid dog year. Dog years cannot be greater than 17 nor less than 0.")
elif  dog_years == 1:
    print(f"The coressponding human year to the entered dog year of {dog_years} year is ", 15)
elif dog_years == 2:
    print(f"The coressponding human year to the entered dog year of {dog_years} years is ", 24)
elif dog_years > 2 and dog_years < 17:
    human_years = 24 + ((dog_years - 2) * 4)
    print(f"The coressponding human year to the entered dog year of {dog_years} years is ", human_years)

# 3. Vowles/Consonants/ y
vowels = ['a','e','i','o','u']
user_char = str(input("Enter a character: "))
if user_char in vowels:
    print("Entered character is a vowel.")
elif user_char == 'y':
    print("Entered character y is sometimes a vowel and sometiumes a consonant.")
else:
    print("Entered character is a consonant.")

# 4. Name of shapes
no_of_sides = int(input("Enter the no of sides of the shape: "))
if no_of_sides < 3 or no_of_sides > 10:
    print("Entered no of sides does not represent any recognized shape.")
elif no_of_sides == 3:
    print("Entered no of sides represent a shape called triangle.")
elif no_of_sides == 4:
    print("Entered no of sides represents a shape called square, rectangle or rhombus.")
elif no_of_sides == 5:
    print("Entered no of sides represents a shape called pentagon.")
elif no_of_sides == 6:
    print("Entered no of sides represents a shape called hexagon.")
elif no_of_sides == 7:
    print("Entered no of sides represents a shape called heptagon.")
elif no_of_sides == 8:
    print("Entered no of sides represents a shape called octagon.")
elif no_of_sides == 9:
    print("Entered no of sides represents a shape called nonagon.")
elif no_of_sides == 10:
    print("Entered no of sides represents a shape called decagon.")

# 5. No of days in a month
mnth = str(input("Enter the full name of a month: "))
mnth = mnth.title()
if mnth == 'February':
    print("The no of days in the entered month is 28 or 29, depending upon the year.")
elif mnth in ['January','March','May','July','August','October','December']:
    print("The no of days in the entered month is 31.")
elif mnth in ['April','June','September','November']:
    print("The no of days in the entered month is 30.")
else:
    print("Please check the name of the month you have entered.")

# 6. Sound decibels
sound_lvl = int(input("Enter a sound level in decibels: "))
if sound_lvl == 40:
    print("The decibel you entered matches the noise QuietRoom.")
elif sound_lvl == 70:
    print("The decibel you entered matches the noise AlarmClock.")
elif sound_lvl == 106:
    print("The decibel you entered matches the noise Gas Lawnmower.")
elif sound_lvl == 130:
    print("The decibel you entered matches the noise Jackhammer.")
elif sound_lvl > 40 and sound_lvl < 70:
    print("The decibel you entered falls in between the noise QuietRoom and AlarmClock.")
elif sound_lvl > 70 and sound_lvl < 106:
    print("The decibel you entered falls in between the noise AlarmClock and Gas Lawnmower.")
elif sound_lvl > 106 and sound_lvl < 130:
    print("The decibel you entered falls in between the noise Gas Lawnmower and Jackhammer.")
elif sound_lvl < 40:
    print("The decibel you entered falls below the noise QuietRoom.")
elif sound_lvl > 130:
    print("The decibel you entered falls above the noise Jackhammer.")

# Wanted to try using Dictionary instead of If & Else   
# 7. Music Frequency
dict = {"C4":261.63,"D4":293.66,"E4":329.63,"F4":349.23,"G4":392,"A4":440,"B4":493.88}
mnote = str(input("Enter a Music Note: "))
if mnote in dict.keys():
    frq = dict[mnote]
    print("The frequency corresponding to the note entered is: ",frq)
else:
    alp = mnote[0]
    n = int(mnote[1])
    ky = alp + "4"
    middlefrq = dict[ky]
    print(f"The middle frequency for {alp} series is: ", middlefrq)
    frq = middlefrq/(24-n)
    print(f"The frequency for {mnote} is: ",frq)

# Wanted to try using Dictionary instead of If & Else   
# 8. Music Frequesncy 2
dict = {"C4":261.63,"D4":293.66,"E4":329.63,"F4":349.23,"G4":392,"A4":440,"B4":493.88}
mfrq = float(input("Enter a Frequency: "))
key_list = list(dict.keys())
val_list = list(dict.values())
position = val_list.index(mfrq)
print("The note corresponding to the frequency entered is: ",key_list[position])

# 9. Color Wavelength
wl = int(input("Enter a Wavelength in nanometers: "))
if wl >= 380 and wl < 450:
    print("The color that matches the entered wavelength is Violet.")
elif wl >= 450 and wl < 495:
    print("The color that matches the entered wavelength is Blue.")
elif wl >= 495 and wl < 570:
    print("The color that matches the entered wavelength is Green.")
elif wl >= 570 and wl < 590:
    print("The color that matches the entered wavelength is Yellow.")
elif wl >= 590 and wl < 620:
    print("The color that matches the entered wavelength is Orange.")
elif wl >= 620 and wl <= 750:
    print("The color that matches the entered wavelength is Red.")
elif wl < 380 or wl > 750:
    print("The wavelength entered is outside of visible spectrum.")

# List Exercise
# 1. Removing outliers
def outlr_func(vals, l, n):
    vals.sort()
    del vals[l-n: l]
    del vals[0:n]
    return vals
user_inpt = []
while True:
    leng = int(input("Enter the length of list: "))
    if leng <= 4:
        print("The length of the list should be minimum of 5. Please enter a value greater than 4.")
    else:
        break
for i in range(0,leng):
     inp =  int(input(f"Enter the {i+1} element of the list: "))
     user_inpt.append(inp)
print("The list created by user: ",user_inpt)
while True:
    outlr = int(input("Enter the no. of outliers to be removed from either side of the list: "))
    if outlr + outlr >=  leng:
        print("Entered no. of outliers should be lesser than the length of the list.")
    else:
        break
print("Calling function to trim the outliers.")
final_inpt = outlr_func(user_inpt, leng, outlr)
print("\nThe list after deleting the outliers: ", final_inpt)
print("The list created by user: ",user_inpt)
# list value changed, as they are mutable.
        
# 2. Splitting of Text.
sp_char = ["'",'"',',','.',':','?',';','-','!']
user_inpt = str(input("Enter a line of text: "))
lt_words = user_inpt.split(" ")
print(lt_words)
for i in range(0, len(lt_words)):
    txt = lt_words[i]
    n = len(lt_words[i])
    if txt[n-1] in sp_char:
        lt_words[i] = txt[:n-1]
print(lt_words)
 
# Loops
# 1. Average value entered by users
n = 0
sum = 0
while True:
    user_val = int(input("Enter a value: "))
    if user_val != 0:
        sum = sum + user_val
        n = n + 1
    elif user_val == 0 and n == 0:
        print("First user input cannot be a zero.")
    else:
        break
avg = sum / n
print("The average of the values entered by user is: ", avg)

# 2. Palindrome
user_inpt = str(input("Enter a string: "))
err = 0
for i in range(0, int(len(user_inpt)/2)):
    if user_inpt[i] != user_inpt[-(i+1)]:
        err = 1
        print("No. The entered string is not a palindrome.")
    else:
        err = 0
if err == 0:
    print("Yes. The entered string is a palindrome.")
         
# 3. Binary to Decimal
others = ['2','3','4','5','6','7','8','9']
user_inpt = input("Enter a number in binary format (1's & 0's'): ")
n = len(user_inpt) -1
val = 0
err = 0
for i in range(0, len(user_inpt)):
    if user_inpt[i] in others:
        print("Enter a valid Binary number.")
        err = 1
        break
    else:
        val = val + (int(user_inpt[i]) * (2 ** n))
        n = n - 1
if err != 1:
    print("The decimal value of the entered number is: ", val)
    
# Dictonary Exercise
# 1. Unique characters in a string
st_dict = {1:"Hello",2:"World!"}
user_inpt = str(input("Enter a string: "))
n = len(st_dict)
st_dict[n+1] = user_inpt
print(st_dict)
uniq_chr = []
for i in range(0, len(st_dict[n+1])):
    if st_dict[n+1][i] not in uniq_chr:
        uniq_chr.append(st_dict[n+1][i])
n = len(uniq_chr)
print(f"\nUnique characters in the string entered by user is {n}. And ther are: \n",uniq_chr)
    
# 2. Longest Word with length.
user_inpt = str(input("Enter a line of text: "))
lst = user_inpt.split(" ")
n=1
dict_str = {}
for i in lst:
    dict_str[n] = i
    n=n+1
print("The split of texts entered by user are stored in dictionary as: \n", dict_str)
len_str = 0
for i in range(1, len(dict_str)+1):
    if len(dict_str[i]) > len_str:
        len_str = len(dict_str[i])
long_text = []
for i in range(1, len(dict_str)+1):
    if len(dict_str[i]) == len_str:
        len_str = len(dict_str[i]) 
        long_text.append(dict_str[i])
print("The longest string is of length: ",len_str)
print("The list of longest words are: ", long_text)

    