# This is a video about dictionaries inside dictionaries from the nested videos module

restaurants = {
    'El Basurero': {
        'address': '32-17 Steinway St, Queens, NY 11103',
        'menu_url': 'https://www.allmenus.com/'
    },
    'SriPraPhai': {
        'address': '64-13 39th Ave, Woodside, NY 11377',
        'menu_url': 'https://sripraphai.com/menu.html'
    }
}
# print(restaurants)
# print(restaurants['SriPraPhai'])

# for i in range(10):
#     print(i)

# numbers = [1,2,3]

# for num in numbers:
#     print(num)

restaurants['Renas place'] = {'address': '328 riceland st danville va 24540',
                              'phone_number': '434-710-3100'}

print(restaurants)

restaurants['Renas place']['url']= 'www.rena.com' 
# please review this i had added brackets to this
print(restaurants['Renas place'])

restaurants['Renas place'].pop('phone_number')
print(restaurants['Renas place'])
