#!/usr/bin/env python

import web
from restaurant_collection import RestaurantCollection

restaurant_collection = RestaurantCollection("restaurants-lesson7.json")

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