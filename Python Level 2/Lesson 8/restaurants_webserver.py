#!/usr/bin/env python

import web
import shared

urls = ( '/restaurants', 'Restaurants',
         '/restaurant/(.*)', 'SpecificRestaurant',
         '/tripdevisor/(.*)', 'TripDevisor',
         '/addRestaurant','AddRestaurant',
         '/score/([0-5])', 'RestaurantsByScore',
         '/', 'Index')

class RestaurantsByScore:
    def GET (self, score):
        score = int(score)
        matching_places = []
        for restaurant_name in restaurants:
            if int(restaurants[restaurant_name].fave) == score:
                matching_places.append(restaurant_name)
            else:
                print '{0} has score {1}'.format(restaurant_name, restaurants[restaurant_name].fave)
        return '\n'.join(sorted(matching_places))

class TripDevisor:
    def GET (self, place):
        output_html = '' # A string, obviously
        # Add some code in here
        return output_html

class AddRestaurant:
    def GET (self):
        with open("tripdevisor-add.html") as html_template:
            output = html_template.read()
        return output

    def POST(self):
        input_data = web.input()
        name = input_data.name
        type = input_data.type
        # Add some code in here to add the input to the internal restaurants data
        # Then save it out (call the function to save the changes)
        # Then send the HTML for the new restaurant back, like for TripDevisor above
        return name, type

class Restaurants:
    def GET(self):
        print restaurants
        web.header('Content-Type', 'text/plain')
        return '\n'.join(sorted(restaurants.keys()))


class SpecificRestaurant:
    def GET (self, name):
        web.header('Content-Type', 'text/plain')
        return str(restaurants[name])


class Index:
    def GET(self):
        return "This is the index page"


restaurants = shared.read_csvfile('restaurants-lesson8.csv')
app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()