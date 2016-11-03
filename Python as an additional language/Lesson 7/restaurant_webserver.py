#!/usr/bin/env python

import web
from restaurant_class import RestaurantCollection

restaurant_object = RestaurantCollection("restaurants-lesson7.csv")

urls = ( '/echo/(.*)', 'Echo',
        '/(.*)', 'Index')

class Echo:
    def GET (self, path):
        return path

class Index:
    def GET(self, path):
        return "You requested nonexistent path {0}".format(path)


app = web.application(urls, globals())
if __name__ == "__main__":
    app.run()