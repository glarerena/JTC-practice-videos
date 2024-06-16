# Application Programming Interface video from JTC

from imdb import Cinemagoer

# create an instance of the Cinemagoer class
ia = Cinemagoer()

# search for a person name
people = ia.search_person('Mel Gibson')
for person in people:
   print(person.personID, person['name'])

# print('0000154')