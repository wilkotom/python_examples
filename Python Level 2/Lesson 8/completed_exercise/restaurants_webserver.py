#!/usr/bin/env python3

import web
import shared

urls = ( '/restaurants', 'Restaurants',
         '/restaurant/(.*)', 'SpecificRestaurant',
         '/tripdeviser/(.*)', 'TripDeviser',
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
                print('{0} has score {1}'.format(restaurant_name, restaurants[restaurant_name].fave))
        return '\n'.join(sorted(matching_places))

class TripDeviser:
    def GET (self, place):
        return generate_response(place)


class AddRestaurant:
    def GET(self):
        with open("tripdeviser-add.html") as html_template:
            output_html = html_template.read()
        output_html = output_html.replace('{{RESTLIST}}', generate_html_rest_list())
        return output_html

    def POST(self):
        # Add some code in here to add the input to the internal restaurants data
        # Then save it out (call the function to save the changes)
        # Then send the HTML for the new restaurant back, like for TripDevisor above
        input_data = web.input()
        name = input_data.name
        type = input_data.type
        cost = input_data.cost
        fave = input_data.fave
        dist = input_data.dist
        restaurants[name] = shared.Restaurant(name, type, cost, fave, dist)
        shared.save_changes(filename,restaurants)
        return generate_response(name)


class Restaurants:
    def GET(self):
        print(restaurants)
        web.header('Content-Type', 'text/plain')
        return '\n'.join(sorted(restaurants.keys()))


class SpecificRestaurant:
    def GET (self, name):
        web.header('Content-Type', 'text/plain')
        return str(restaurants[name])


class Index:
    def GET(self):
        return "This is the index page"

def generate_html_rest_list():
    list_entry = '<li><a href="/tripdeviser/{0}">{0}</a></li>'
    html_output_fragment  = ''
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


filename = 'restaurants-lesson8.csv'
restaurants = shared.read_csvfile(filename)
app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()
