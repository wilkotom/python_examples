#!/usr/bin/env python

import web
from restaurant_class import RestaurantCollection

restaurant_object = RestaurantCollection("restaurants-lesson7.csv")

urls = ( '/restaurant/(.*)', 'RestaurantJson',
        '/(.*)', 'Index')

class RestaurantJson:
    def GET(self, name):
        return restaurant_object.get_restaurant_json(name)

class Index:
    def GET(self, path):
        return "You requested nonexistent path {0}".format(path)


app = web.application(urls, globals())
if __name__ == "__main__":
    app.run()