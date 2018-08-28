#!/usr/bin/env python3

import web
import shared

urls = ( '/restaurants', 'Restaurants',
         '/restaurant/(.*)', 'SpecificRestaurant',
         '/score/([1-5])', 'RestaurantsByScore',
         '/', 'Index')

class RestaurantsByScore(object):
    def GET (self, score):
        score = int (score)
        # List the restaurants with a particular score
        return # Them

        

class Restaurants(object):
    def GET(self):
        print(restaurants)
        web.header('Content-Type', 'text/plain')
        return '\n'.join(restaurants.keys())


class SpecificRestaurant(object):
    def GET (self, name):
        web.header('Content-Type', 'text/plain')
        return str(restaurants[name])


class Index(object):
    def GET(self):
        return "This is the index page"


restaurants = shared.read_csvfile('restaurants-lesson7.csv')
app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()
