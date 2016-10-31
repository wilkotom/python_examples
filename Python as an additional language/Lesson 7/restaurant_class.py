import csv
import json


class RestaurantCollection:
    """Details of a collection of restaurants, plus various methods to query and update the collection"""

    class Restaurant:
        """Holds details of an individual place to eat"""

        def __init__(self, name, type, cost, fave, dist):
            self.name = name
            self.type = type
            self.cost = cost
            self.fave = fave
            self.dist = dist

        def __str__(self):
            return "{0} is a {1} place {4} minutes from here. Star rating {2}, Cost {3}".format(
                self.name, self.type, self.cost, self.fave, self.dist)


    def __init__(self, file_name):
        self.restaurants = {}
        self.read_jsonfile(file_name)
        self.finished = False
        self.filename = file_name

    def get_restaurant_json(self, restaurant_name):
        return json.dumps(self.restaurants[restaurant_name])

    def get_restaurants_by_score(self, score):
        places = []
        for place in self.restaurants.keys():
            if int(self.restaurants[place].fave) == score:
                places.append(place)
        return json.dumps(places)
        
    def menu(self):
        """Displays a menu and prompts the user for their choice"""
        print "1: Search based on distance"
        print "2: Search based on rating"
        print "3: Add a new entry"
        print "4: Save changes"
        print "5: Exit"

        choice = raw_input("Please enter choice: ")
        if choice == "1":
            self.search_on_distance(raw_input("Please enter max distance: "))
        elif choice == "2":
            self.search_on_rating(raw_input("Please enter minimum rating: "))
        elif choice == "3":
            self.add_restaurant()
        elif choice == "4":
            self.save_changes_as_json(self.filename)
        elif choice == "5":
            self.finished = True
        else:
            print "That's not a valid choice - try again!"

    def search_on_distance(self, dist):
        """Prints out all restaurants within a given distance"""
        for restaurant_name in self.restaurants.keys():
            rest_details = self.restaurants[restaurant_name]
            if int(rest_details.dist) <= int(dist):
                print rest_details

    def search_on_rating(self, rating):
        """Prints out all restaurants with a given rating or better"""
        for restaurant_name in self.restaurants.keys():
            rest_details = self.restaurants[restaurant_name]
            if int(rest_details.fave) >= int(rating):
                print rest_details

    def add_restaurant(self):
        """Prompts the user for a new restaurant to add to the database"""
        name = raw_input("Enter Restaurant Name: ")
        cuisine = raw_input("Enter Restaurant type: ")
        cost = raw_input("Enter Restaurant cost (out of 5): ")
        fave = raw_input("Enter cost (out of 5): ")
        dist = raw_input("Enter distance (minutes' walk): ")
        self.restaurants[name] = {"type": cuisine, "cost": cost,
                                  "fave": fave, "dist": dist}

    def read_csvfile(self, filename):
        """Reads the restaurant list from a CSV file"""
        restaurants = {}
        with open(filename) as csvfile:
            csv_reader = csv.DictReader(csvfile)
            for rest_details in csv_reader:
                restaurants[rest_details['name']] = self.Restaurant(**rest_details)
        return restaurants

    def save_csvfile(self, filename):
        """Saves the restaurant data as CSV"""
        csv_writer = csv.DictWriter(filename, fieldnames=['name', 'type', 'cost', 'fave', 'dist'])
        csv_writer.writeheader()
        for restaurant in self.restaurants.keys():
            out_dict = {"name": self.restaurants[restaurant].name,
                        "type": self.restaurants[restaurant].type,
                        "cost": self.restaurants[restaurant].cost,
                        "fave": self.restaurants[restaurant].fave,
                        "dist": self.restaurants[restaurant].dist}
            csv_writer.writerow(out_dict)

    def read_jsonfile(self, filename):
        raw_restaurants = {}
        """Saves the restaurant data as JSON"""
        filename = filename.replace('csv', 'json')
        with open(filename, 'r') as jsonfile:
            raw_restaurants = json.load(jsonfile)
        for restaurant_name in raw_restaurants:
            raw_restaurants[restaurant_name]["name"] = restaurant_name
            self.restaurants[restaurant_name] = self.Restaurant(**raw_restaurants[restaurant_name])

