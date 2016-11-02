#!/usr/bin/env python

import httplib
import json

arguments = '?api_key=XXXXXXXXXXXX'

connection = httplib.HTTPSConnection('api.themoviedb.org')
connection.request('GET', '/3/genre/movie/list'+ arguments)
response = connection.getresponse()
response_data = response.read()
connection.close()

print 'Response code was {0}'.format(response.status)
print 'Response was: {0}'.format(response_data)


