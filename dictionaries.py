# # blank_dict = {}
# # print(blank_dict)
# # print(type(blank_dict))

# # # created a dictionary added key value pairs
# # user_account = {'username': 'Rena', 'balance': 41}
# # print(user_account)

# # # access value by using key
# # print(user_account['balance'])

# learning_dict = {
#     'username': 'Rena',
#     'balance': 100,
#     'fun': True,
#     'money': [100,25,41]
# }

# print(learning_dict)

# # adding key value pairs 
# learning_dict['learning'] = True 
# print(learning_dict)

# # update key value pairs
# learning_dict['balance'] = 41233
# print(learning_dict)

# print(learning_dict['money'][0])

# # assign the list inside the dictionary to a variable
# cash = learning_dict['money']
# print(cash)

# learning_dict['money'].append(101)
# print(learning_dict)
# print(cash)

# # remove key value pairs 
# learning_dict.pop('fun')
# print(learning_dict)

# lists vs. dictionaries 

a = [] # this is an empty list
b = {} # this is an empty dictionary

# we can use type with a print statement to find out data type

# add items to list 
a.append('Rena')
a.append('Ann')
a.append('Glare')

print(a)
print(a[2])

# add key/value pairs to dictionary
b['firstname'] = 'Rena'
b['lastname'] = 'Glare'
b['cool'] = True

print(b)
print(b['lastname'])
