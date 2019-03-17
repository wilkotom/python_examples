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
    return generate_response(place)


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
    output = output.replace('{{RESTLIST}}', generate_html_rest_list())
    return output


@post('/addRestaurant')
def add_new_restaurant():
    name = request.forms.get('name')
    cuisine = request.forms.get('type')
    cost = request.forms.get('cost')
    fave = request.forms.get('fave')
    dist = request.forms.get('dist')
    restaurants[name] = shared.Restaurant(name, cuisine, cost, fave, dist)
    shared.save_changes(filename, restaurants)
    return generate_response(name)


def generate_html_rest_list():
    list_entry = '<li><a href="/tripdeviser/{0}">{0}</a></li>'
    html_output_fragment = ''
    for restaurant_name in sorted(restaurants):
        html_output_fragment = html_output_fragment + list_entry.format(restaurant_name)
    return html_output_fragment


def generate_response(name):
    with open("tripdeviser.html") as html_template:
        output_html = html_template.read()
    output_html = output_html.replace('{{RESTLIST}}', generate_html_rest_list())
    output_html = output_html.replace('{{PLACENAME}}', name)
    output_html = output_html.replace('{{PLACEDESCRIPTION}}', str(restaurants[name]))
    return output_html


if __name__ == "__main__":
    filename = 'restaurants-lesson8.csv'
    restaurants = shared.read_csvfile(filename)
    print(restaurants)
    run(host='localhost', port=8080)
