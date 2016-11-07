#!/usr/bin/env python

import web
import json
from restaurant_class import RestaurantCollection

restaurant_object = RestaurantCollection("restaurants-lesson8.json")

urls = ( '/restaurants/(.*)', 'RestaurantJson',
         '/score/([0-5])','RestaurantsByScore',
        '/(.*)', 'Index')

class RestaurantJson:
    def GET (self, name):
        return json.dumps(restaurant_object[name].as_dict())

class RestaurantsByScore:
    def GET (self, score):
        score = int(score)
        return json.dumps(restaurant_object.get_restaurants_by_score(score))

class Index:
    def GET(self, path):
        return "You requested nonexistent path {0}".format(path)


app = web.application(urls, globals())
if __name__ == "__main__":
    app.run()