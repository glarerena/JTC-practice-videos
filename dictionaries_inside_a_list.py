a = [{}, {}, {}]
print(a)
print(type(a))


users = [
    {'username': 'alanna', 'password': 'javascript', 'last_login': '9/28/2020'},
    {'username': 'aryn', 'password': 'dictionaries'},
    {'username': 'yusuf', 'password': 'django', 'last_login': '9/26/2020'},
    {'username': 'paul', 'password': 'github'}
]

# print(users)
print(users[2])
print(users[2]['password'])

users.append({'username': 'rena', 'password': 'glare'})
print(users)

print(users[-1])

users[-1]['verified account'] = True
print(users[-1])

# we used the pop and append method to take off and add things to the list
# we accessed the list inside the dictionary by using indexing 
