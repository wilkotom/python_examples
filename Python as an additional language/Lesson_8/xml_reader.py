#!/usr/bin/python

import xml.etree.ElementTree as XMLElementTree

filename = "Restaurants_Example_1.xml"

xmlfile = XMLElementTree.parse(filename)

restaurants = {}

print xmlfile.getroot()

for element in xmlfile.getroot():
    print element
    rest_details = {}
    for subelement in element:
        print subelement.text, subelement.tag
        rest_details[subelement.tag] = subelement.text
    restaurants[rest_details['name']] =  rest_details
    del restaurants[rest_details['name']]['name']

print restaurants