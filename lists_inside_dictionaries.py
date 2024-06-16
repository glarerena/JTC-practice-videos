# Lists inside dictionaries example with a shopping cart

cart = {
    'fruits': ['oj', 'grapes', 'strawberries'],
    'vegatables': ['carrots', 'spinach', 'peas'],
    'total_price': 23.21
}
print(cart)
print(type(cart))
print(type(cart['vegatables']))
print(cart['vegatables'])
print(cart['vegatables'][0])