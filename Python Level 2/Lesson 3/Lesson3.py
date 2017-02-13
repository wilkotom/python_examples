#!/usr/bin/env python
import shared

restaurants = {}

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
        # You'll need to update the below to use properties, such as rest_details.name
        # instead of dictionary references (like rest_details['name'])
        if int(rest_details["dist"]) <= int(dist):
            print restaurant_name + " is a " + rest_details["type"] + " place " + \
             rest_details["dist"] + " minutes from here"
      

def search_on_rating(rating):
    score = shared.return_verified_value(1,5,rating)
    for restaurant_name in restaurants.keys():
        rest_details = restaurants[restaurant_name]
        if int(rest_details["fave"]) >= int(score):
            print restaurant_name + " is a " + rest_details["fave"] + "/5 rated place " + \
              str(rest_details["dist"]) + " minutes from here"

def add_restaurant():
    name = raw_input("Enter Restaurant Name: ")
    cuisine = raw_input("Enter Restaurant type: ")
    cost = raw_input("Enter Restaurant cost (out of 5): ")
    fave = raw_input("Enter cost (out of 5): ")
    dist = raw_input("Enter distance (minutes' walk): ")
    # Change this to use a Restaurant instead of a dictionary as well.
    restaurants[name] = {"type": cuisine, "cost": cost, 
                         "fave": fave, "dist": dist}


shared.read_csvfile(restaurants)

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
        shared.save_changes(restaurants)
    elif choice == "5":
        finished = True
    else:
        print "That's not a valid choice - try again!"
