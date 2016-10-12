#!/usr/bin/env python

import shared

filename = 'restaurants-lesson4.csv'

finished = False


def show_menu():
    print "1: Search based on distance"
    print "2: Search based on rating"
    print "3: Add a new entry"
    print "4: Save changes"
    print "5: Exit"


def search_on_distance(dist):
    for restaurant_name in restaurants.keys():
        rest_details = restaurants[restaurant_name]
        if int(rest_details.dist) <= int(dist):
            print restaurant_name + " is a " + rest_details.type + " place " + \
                  str(rest_details.dist) + " minutes from here"


def search_on_rating(rating):
    score = shared.return_verified_value(1, 5, rating)
    for restaurant_name in restaurants.keys():
        if restaurants[restaurant_name].fave >= score:
            print restaurant_name + " is a " + str(restaurants[restaurant_name].fave) + "/5 rated place " + \
                  str(restaurants[restaurant_name].dist) + " minutes from here"



def add_restaurant():
    name = raw_input("Enter Restaurant Name: ")
    cuisine = raw_input("Enter Restaurant type: ")
    cost = raw_input("Enter Restaurant cost (out of 5): ")
    fave = raw_input("Enter star rating (out of 5): ")
    dist = raw_input("Enter distance (minutes' walk): ")
    restaurants[name] = shared.Restaurant(name, cuisine, cost, fave, dist)



restaurants = shared.read_csvfile(filename)

while not finished:
    show_menu()
    choice = raw_input("Please enter choice: ")
    if choice == "1":
        search_on_distance(raw_input("Please enter max distance: "))
    elif choice == "2":
        search_on_rating(raw_input("Please enter minimum rating: "))
    elif choice == "3":
        add_restaurant()
    elif choice == "4":
        shared.save_changes(filename,restaurants)
    elif choice == "5":
        finished = True
    else:
        print "That's not a valid choice - try again!"
