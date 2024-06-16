# Handling Exceptions

# try / except block

# x = 365
# SAY FOR INSTANCE WE DID NOT DEFINE X SO IT WILL RUN THE EXCEPT BLOCK

# try:
#     # try to run this block of code
#     print(x)

# except:
#     # if an exception exists, run this block of code
#     print('Something went wrong')

# Multiple Exceptions

# x = 100

# try:
#     print(x)
# except NameError:
#     print('Variable is not defined.')
# except:
#     print('Something else went wrong.')


# we can also add an else statement
# it can say nothing went wrong

# Finally
# Finally always runs if there is an exception or not

x = 'Finished'
try:
    print(x)
except:
    print('Something went wrong.')
finally:
    print('We made it to the end.')
