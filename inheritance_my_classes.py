# so in the video he has removed all of the classes in the inheritance demo video
# all he has left in the demo.py file is the instances 
# so he made an import statement for us using the * universal selector to get them all

# this import statement below allows me to import all of the classes from that file
# so i am able to use all of the classes in this file 

# from inheritance_demo import *

# once you do that that, it will create a __pycache__ folder
# that is like an intermediary between the two files 
# please do not post this to github as it is not necessary



# this is the last video of the inheritance series
# we are creating a parent and child class

# parent class

class AccountHolder():
    def __init__(self, username):
        self.username = username

    def display_info(self):
        print(f'Account for user: {self.username}')

# Creating an instance of AccountHolder
account7 = AccountHolder(username='Molly Glare')
account7.display_info()

