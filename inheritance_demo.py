# parent class
class Account():
    def __init__(self, username):
        self.username = username

    def display_info(self):
        print(f'Account for user: {self.username}')

# Testing the Account class
account1 = Account(username='Rena Glare')
account1.display_info()

# second parent class
class TwitterUser():
    def __init__(self, twitter_handle):
        self.twitter_handle = twitter_handle

    def display_twitter(self):
        print(f'Twitter handle: {self.twitter_handle}')

# Creating a new instance of TwitterUser with an f-string
account4 = TwitterUser(twitter_handle='@new_twitter_handle')
print(f'Created a new Twitter account: {account4.twitter_handle}')

# child class combining both parent classes
class TwitterAccount(Account, TwitterUser):
    def __init__(self, username, password, twitter_handle):
        Account.__init__(self, username)
        TwitterUser.__init__(self, twitter_handle)
        self.password = password

# use the super() method to refer to the parent class
class Guest(Account):
    def __init__(self, username, email):
        # used the account method to get rid of the username
        # used the super() method to refer to the parent class no matter the name 
        super().__init__(username)
        self.email = email

    def display_info(self):
        print(f'Account for user: {self.username} with email address {self.email}.')

# Testing the Guest class
account2 = Guest(username="Born Glare", email='bglare@yahoo')
account2.display_info()
print(account2.email)

# new child class using multiple inheritance
class StandardUser(Account, TwitterUser):
    def __init__(self, username, password, twitter_handle):
        # used the account method to get rid of the username
        # used the super() method to refer to the parent class no matter the name
        Account.__init__(self, username)
        TwitterUser.__init__(self, twitter_handle)
        self.password = password

    def login(self):
        password_attempt = input('Please Enter Your Password: ')
        if password_attempt == self.password:
            print('Logged in.')
        else:
            print('Try again please.')

    def display_info(self):
        print(f'Account for user: {self.username} with a protected password and Twitter handle {self.twitter_handle}.')

# Testing the StandardUser class
account3 = StandardUser(username='Daisy', password='daisy123', twitter_handle='@daisy123')

# Uncomment the line below to test the login method
# account3.login()

print(type(account1))
account1.display_info()
print(type(account2))
account2.display_info()
print(type(account3))
account3.display_info()

# Printing account4
print(type(account4))
account4.display_twitter()




