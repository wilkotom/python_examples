#!/usr/bin/env python

import web
from restaurant_class import Restaurant

restaurant_object = Restaurant("restaurants-lesson8.csv")

urls = ( '/restaurants/(.*)', 'RestaurantJson',
        '/score/([0-5])', 'RestaurantsByScore',
        '/(.*)', 'Index')

class RestaurantJson:
    def GET(self, name):
        return restaurant_object.get_restaurant_json(name)


class RestaurantsByScore:
    def GET(self, score):
        score = int(score)
        return restaurant_object.get_restaurants_by_score(score)


class Index:
    def GET(self, path):
        return "You requested nonexistent path {0}".format(path)


app = web.application(urls, globals())
if __name__ == "__main__":
    app.run()