import httplib
import json

api_key = 'XXXXXX'
hostname = 'api.themoviedb.org'
connection = httplib.HTTPSConnection('api.themoviedb.org')

api_path = '/3'


def get_object(path):
    request_path = "{0}{1}?api_key={2}".format(api_path, path, api_key)
    connection = httplib.HTTPSConnection('api.themoviedb.org')
    connection.request('GET', request_path)
    response = connection.getresponse()
    response_body = response.read()
    connection.close()
    return json.loads(response_body)

request_path = "/genre/movie/list"
response_data = get_object(request_path)
genres = response_data['genres']


menu_option_number = 1
menu_options = []
for genre_definition in genres:
    menu_options.append(genre_definition)
    print "{0}: {1}".format(menu_option_number,genre_definition['name'])
    menu_option_number += 1

genre_choice = -1
while genre_choice < 0 or genre_choice >= len(menu_options):
    try:
        genre_choice = int(raw_input("Please enter genre number:")) -1
    except ValueError:
        print "That's not a number"



tvdb_genre_id = menu_options[genre_choice]['id']

movies_path = "/genre/{0}/movies".format(tvdb_genre_id)
movies_data = get_object(movies_path)

movies = movies_data['results']

# Two ways to solved this - first way, using a dictionary with the budget as the key

movie_budgets = {}

for movie in movies:
    movie_details = get_object('/movie/{0}'.format(movie['id']))
    budget = movie_details['budget']
    if budget in movie_budgets.keys():
        movie_budgets[budget].append(movie_details['title']) # more than one movie can have the same budget,
                                                             # so we store all the movies with a given budget in a list
    else:
        movie_budgets[budget] = [movie_details['title']]

for budget in sorted(movie_budgets.keys(), reverse=True):
    for movie in movie_budgets[budget]:
        print u"{0}\t\t{1}".format(budget, movie)


#  Second way, using the title as the key but sorting on the budget using a lambda function.
# <dictionary>.items() returns a list of tuples of the form (key, value).

all_movie_details = {}
for movie in movies:
    all_movie_details[movie['title']] =  get_object('/movie/{0}'.format(movie['id']))

for (movie_title, details) in sorted(all_movie_details.items(), reverse=True, key=lambda (t, m): m['budget']):
    print u"{0}\t\t{1}".format(details['budget'], movie_title)


# Second way (again) using an explicit function inteadt of an anonymous one

def get_budget(details):
    # details is a tuple consisting of (key, value) as pulled from the dictionary items() method
    return details[1]['budget']

all_movie_details = {}
for movie in movies:
    all_movie_details[movie['title']] =  get_object('/movie/{0}'.format(movie['id']))

for (movie_title, details) in sorted(all_movie_details.items(), reverse=True, key=get_budget):
    print u"{0}\t\t{1}".format(details['budget'], movie_title)
