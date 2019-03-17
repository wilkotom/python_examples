#!/usr/bin/env python3

from bottle import get, request, response, run, post
import shared


@get('/')
def index():
    return "This is the index page"


@get('/restarants')
def all_restaurants():
    print(restaurants)
    response.set_header('Content-Type', 'text/plain')
    return '\n'.join(restaurants.keys())


@get('/restaurants/<restaurant>')
def specific_restaurant(restaurant):
    response.set_header('Content-Type', 'text/plain')
    return str(restaurants[restaurant])


@get('/tripdeviser/<place>')
def trip_deviser(place):
    output_html = ''  # A string, obviously
    # Add some code in here
    return output_html


@get('/score/<score:re:[1-5]>')
def restaurants_by_score(score):
    places = []
    for place in restaurants.values():
        if int(place.fave) >= int(score):
            places.append(str(place))
    return '<br/>'.join(places)


@get('/addRestaurant')
def display_add_restaurant_form():
    with open("tripdeviser-add.html") as html_template:
        output = html_template.read()
    return output


@post('/addRestaurant')
def add_new_restaurant():
    name = request.forms.get('name')
    cuisine = request.forms.get('cuisine')
    # Add some code in here to add the input to the internal restaurants data
    # Then save it out (call the function to save the changes)
    # Then send the HTML for the new restaurant back, like for TripDeviser above
    return name, cuisine


if __name__ == "__main__":
    restaurants = shared.read_csvfile('restaurants-lesson8.csv')
    run(host='localhost', port=8080)
