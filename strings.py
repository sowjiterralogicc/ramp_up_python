# #print of a string
# print("Hello")
# #assigning that string to a variable
# s="Hello"
# print(s)
# #multiline string
# s1="""This is string
# python program"""
# print(s1)
# # How to Access Characters of a String?
# # We can access characters of a string by using the following ways.
# # 1) By using index
# # 2) By using slice operator
# #to get the first character of a string
# s="Hello"
# print(s[1])

# Q) Write a Program to Accept some String from the Keyboard and display its 
#  Characters by Index wise (both Positive and Negative Index)
# s=input("Enter a string: ")
# x=0
# print(x-len(s))
# for i in s:
#     print(x,x-len(s),i)
#     x=x+1

# 2)Accessing Characters by using Slice Operator:
#  Syntax: s[bEginindex:endindex:step]
#  Begin Index: From where we have to consider slice (substring)
#  End Index: We have to terminate the slice (substring) at endindex-1 
#  Step: Incremented Value.

# Behaviour of Slice Operator:
# 1) s[bEgin:end:step]
# 2) Step value can be either +ve or –ve
# 3) If +ve then it should be forward direction(left to right) and we have to consider bEgin 
# to end-1
# 4) If -ve then it should be backward direction (right to left) and we have to consider bEgin 
# to end+1.


# ***Note:
#  In the backward direction if end value is -1 then result is always empty.
#  In the forward direction if end value is 0 then result is always empty.

# Mathematical Operators for String:
# We can apply the following mathematical operators for Strings.
# 1) + operator for concatenation
# 2) * operator for repetition

#  print("durga"+"soft")  durgasoft
#  print("durga"*2)  durgadurga

# Note: 
# 1) To use + operator for Strings, compulsory both arguments should be str type.
# 2) To use * operator for Strings, compulsory one argument should be str and other
# argument should be int.


#  Write a Program to access each Character of String in 
#  Forward and Backward Direction by using while Loop?

# s="sowjanya"
# n=len(s)
# i=0
# print("forward direction")
# while i<n:
#     print(s[i],end=' ')
#     i=i+1
# i=-1
# print("backword direction")
# while i>=-n:
#     print(s[i],end=' ')
#     i=i-1

# Checking Membership:
# We can check whether the character or string is the member of another string or not by 
# using in and not in operators

# Checking Membership:
# We can check whether the character or string is the member of another string or not by 
# using in and not in operators
# s = 'durga'
# print('d' in s)  True
# print('z' in s)  False
# 1) s = input("Enter main string:") 
# 2) subs = input("Enter sub string:") 
# 3) if subs in s: 
# 4) print(subs,"is found in main string") 
# 5) else: 
# 6) print(subs,"is not found in main string")



# Comparison of Strings:
#  We can use comparison operators (<, <=, >, >=) and equality operators (==, !=) for 
# strings.
#  Comparison will be performed based on alphabetical order.
# 1) s1=input("Enter first string:") 
# 2) s2=input("Enter Second string:") 
# 3) if s1==s2: 
# 4) print("Both strings are equal") 
# 5) elif s1<s2: 
# 6) print("First String is less than Second String") 
# 7) else: 
# 8) print("First String is greater than Second String")

# Removing Spaces from the String:
# We can use the following 3 methods
# 1) rstrip()  To remove spaces at right hand side
# 2) lstrip() To remove spaces at left hand side
# 3) strip()  To remove spaces both sides


# Counting substring in the given String:
# We can find the number of occurrences of substring present in the given string by using 
# count() method.
# 1) s.count(substring)  It will search through out the string.
# 2) s.count(substring, bEgin, end)  It will search from bEgin index to end-1 index.
# Finding Substrings:
# We can use the following 4 methods
# For forward direction:
# 1) find()
# 2) index()
# For backward direction:
# 1) rfind()
# 2) rindex()

# Replacing a String with another String:
# s.replace(oldstring, newstring)
# inside s, every occurrence of old String will be replaced with new String.

# Splitting of Strings:
#  We can split the given string according to specified seperator by using split() method.
#  l = s.split(seperator)
#  The default seperator is space. The return type of split() method is List.

# Joining of Strings:
# We can join a Group of Strings (List OR Tuple) wrt the given Seperator.
# s = seperator.join(group of strings)
# Eg 1:
# t = ('sunny', 'bunny', 'chinny')
# s = '-'.join(t)
# print(s)
# Output: sunny-bunny-chinny

# Changing Case of a String:
# We can change case of a string by using the following 4 methods.
# 1) upper()  To convert all characters to upper case
# 2) lower()  To convert all characters to lower case
# 3) swapcase()  Converts all lower case characters to upper case and all upper case 
# characters to lower case
# 4) title()  To convert all character to title case. i.e first character in every word should 
# be upper case and all remaining characters should be in lower case.
# 5) capitalize()  Only first character will be converted to upper case and all remaining 
# characters can be converted to lower case 
# 1) s = 'learning Python is very Easy' 
# 2) print(s.upper()) 
# 3) print(s.lower()) 
# 4) print(s.swapcase()) 
# 5) print(s.title()) 
# 6) print(s.capitalize())

# To Check Type of Characters Present in a String:
# Python contains the following methods for this purpose.
# 1) isalnum(): Returns True if all characters are alphanumeric( a to z , A to Z ,0 to9 )
# 2) isalpha(): Returns True if all characters are only alphabet symbols(a to z,A to Z)
# 3) isdigit(): Returns True if all characters are digits only( 0 to 9)
# 4) islower(): Returns True if all characters are lower case alphabet symbols
# 5) isupper(): Returns True if all characters are upper case aplhabet symbols
# 6) istitle(): Returns True if string is in title case
# 7) isspace(): Returns True if string contains only spaces

# # #looping the letters of a string
# for i in s:
#     print(i)

# #how to find length of a string
# s="sowji"
# print(len(s))

# #how to check whether the particular letters or words present in a string
# s="python is a very easy language"
# print("is" in s)

# #above program using condition
# if "is" in s:
#     print("yes, present in string s")

#write a program to reverse a string
s="ammu"
n=len(s)-1
reversed_string=""
while n>=0:
    reversed_string=reversed_string+s[n]
    n=n-1
print(reversed_string)

