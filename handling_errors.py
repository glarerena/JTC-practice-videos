# ''' 
# 1. Understanding Trace Back
# 2. Common Error Types
# 3. Handling Exceptions in buggy code'''


# # Traceback

# def favorite_ice_cream():
#     ice_creams = [
#         'vanilla',
#         'chocolate',
#         'mint chocolate chip'
#     ]
#     print(ice_creams[2])

# favorite_ice_cream()  

# # This code gives us a traceback error
# # This says list index out of range 
# # It tells each line on where the error is 
# # I fixed the error by changing the index, but it was originally indexing [3]

# print('Hello World')
# Here is an example below of a syntax error 
# This shows an unterminated string literal detected with the line number
# print('Hello World)

# Indentation Error
# this says expected an indented block after function definition on line 29
# The return statement also is red and underlined showing me there is an issue
# To fix this I just tabbed one time
# def multiply(a,b):
#     return a * b


# print(multiply(2,2))

# Tab Error
# TabError: inconsistent use of tabs and spaces in indentation
# Python3 does not allow you to mix tabs and spaces
# To help with this, you can fix the settings
# Or you can use an extension like Prettier
# But please make sure you understand what code should be where in Python
# def some_function():
#     msg = 'Hello Rena'
#     print(msg)
#     return msg

# some_function()


# Name Errors
# b = 3
# a = b + 2
# print(a)
# This is returning name error: name 'b' is not defined

# Index Error

# it does return the oranges part that we called back
# but we do not have index items 3
# index error list index out of range
# groceries = ['apples', 'soda', 'oranges']
# print(groceries[2])
# print(groceries[3])

# Type Error

# def square_num(num):
#     return num * num

# # print(square_num('abc'))
# print(square_num(7))






