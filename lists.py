# lists video
# courses = [ 'Math', 'History', 'Gym', 'Biology' ]
# print(courses)

# index at the list 
# print(courses[0])

# # get the last value of the list 
# print(courses[-1])

# # range of values
# print(courses[0:2])

# # can leave off the beginning or the 0 it produce same results
# print(courses[:2])

# # can leave off the ending so it will go to the end 
# print(courses[2:])

# list methods
# append
# courses.append('Art')
# print(courses)

# insert method takes 2 arguments
# location, then value
# courses.insert(0, 'Art')
# print(courses)

# extend method
# use this when we want to add multiple values to our list
# courses_2 = ['Art', 'Music']
# courses.extend(courses_2)
# print(courses)

# # remove some values from a list
# # remove method
# courses.remove('Math')
# print(courses)

# pop method takes off the last item in the list
# helpful for a stack or a queue
# pop returns the value that has been removed 

# popped = courses.pop()
# print(popped)
# print(courses)

# sorting lists
# reverse method
# courses.reverse()
# print(courses)

# #this returns items in abc order
# courses.sort()

# # if the list contained numbers then it would return it in ascending order

# nums = [1, 2, 5, 10, 100, 24, 3]
# # nums.sort()
# # print(nums)

# # courses.sort(reverse=True)
# # nums.sort(reverse=True)

# # print(courses)
# # print(nums)

# sorted_courses = sorted(courses)
# print(sorted_courses)

# my_list = [1, 2, 3, 4, 5]
# print(my_list[2])


# min max and sum for numbers functions 
# numz = [ 2, 3, 4, 5, 6]
# print(min(numz))
# print(max(numz))
# print(sum(numz))


# index example
# courses = [ 'Math', 'History', 'Gym', 'Biology' ]
# print(courses.index('Math'))

# # in method for Boolean value return

# print('Art' in courses)

# # for loop with the in method

# for item in courses: 
#     print(item)
# item is just a variable not a keyword

# an indexed for loop for the list 
# for index, learning in enumerate(courses):
#     print(index, learning)


# string method using .join
# course_str = ', '.join(courses)
# print(course_str)
# course_str = ' - '.join(courses)
# print(course_str)

# # split method
# # turn a string back into a list
# new_list = course_str.split(' - ')
# print(new_list)


