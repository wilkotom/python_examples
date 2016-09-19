#!/usr/bin/env python

import csv

restaurants = {}

finished = False


def show_menu():
    print "1: Search based on distance"
    print "2: Search based on rating"
    print "3: Exit" 
    
    
def search_on_distance(dist):
    for restaurant_name in restaurants.keys():
        rest_details = restaurants[restaurant_name]
        if int(rest_details["dist"]) <= int(dist):
            print restaurant_name + " is a " + rest_details["type"] + " place " + \
             rest_details["dist"] + " minutes from here"
      
              
def search_on_rating(rating):
    for restaurant_name in restaurants.keys():
        rest_details = restaurants[restaurant_name]
        if int(rest_details["fave"]) >= int(rating):
            print restaurant_name + " is a " + rest_details["fave"] + "/5 rated place " + \
              str(rest_details["dist"]) + " minutes from here"


with open("restaurants-lesson8.csv") as csvfile:
    csv_reader = csv.DictReader(csvfile)
    for rest_details in csv_reader: 
        restaurant_name = rest_details['name']
        del rest_details['name']
        restaurants[restaurant_name] =  rest_details



while not finished:
    show_menu()
    choice=raw_input("Please enter choice: ")
    if choice == "1":
        search_on_distance(raw_input("Please enter max distance: "))
    elif choice == "2":
        search_on_rating(raw_input("Please enter minimum rating: "))
    elif choice == "3":
        finished = True
    else:
        print "That's not a valid choice - try again!"
        
 
