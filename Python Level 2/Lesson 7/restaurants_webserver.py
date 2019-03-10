#!/usr/bin/env python3

from bottle import get, response, run
import shared

@get('/')
def index():
    return "This is the index page"


@get('/restarants')
def all_restaurants(self):
    print(restaurants)
    response.set_header('Content-Type', 'text/plain')
    return '\n'.join(restaurants.keys())


@get('/restaurants/<restaurant>')
def specific_restaurant(restaurant):
    response.set_header('Content-Type', 'text/plain')
    return str(restaurants[restaurant])

@get('/hello/<name:re:[A-Z][a-z]*>')
def say_hello(name):
    return f"Why hello there, {name}"


@get('/score/<score>')
def restaurants_by_score (score):
    # check that the score provided is one of the digits 1-5
    # hint: use a regular expression match
    score = int (score)
    #  get the restaurants with a particular score
    return # those restaurants


restaurants = shared.read_csvfile('restaurants-lesson7.csv')

if __name__ == "__main__":
    run(host='localhost', port=8080)
