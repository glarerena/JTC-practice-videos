# parent class
class Account():
    def __init__(self, username):
        self.username = username

    def display_info(self):
        print(f'Account for user : {self.username}')

account1 = Account(username='Rena Glare')
account1.display_info()

# child class

# use the super() method to refer to the parent class
class Guest(Account):
    def __init__(self, username, email):
        # used the account method to get rid of the username
        # used the super() method to refer to the parent class no matter the name 
        super().__init__(username)
        self.email = email

    def display_info(self):
        print(f'Account for user : {self.username} with email address {self.email}.')

account2 = Guest(username="Born Glare", email='bglare@yahoo')
account2.display_info()
print(account2.email)

# new child class
class StandardUser(Account):
    def __init__(self, username, password):
        super().__init__(username)
        self.password = password

    def login(self):
        password_attempt = input('Please Enter Your Password: ')
        if password_attempt == self.password:
            print('Logged in.')
        else:
            print('Try again please.')

    def display_info(self):
        print(f'Account for user : {self.username} with a protected password.')

account3 = StandardUser(username='Daisy', password='daisy123')

# Uncomment the line below to test the login method
# account3.login()

print(type(account1))
account1.display_info()
print(type(account2))
account2.display_info()
print(type(account3))
account3.display_info()


