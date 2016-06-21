import csv
import json

class Restaurant:


    def __init__(self, csv_file_name):
        self.restaurants = {}
        self.finished = False
        self.filename = csv_file_name
        self.read_jsonfile(csv_file_name)
    
    def get_restaurant_json(self, restaurant_name):
        return json.dumps(self.restaurants[restaurant_name])

    def get_restaurants_by_score(self, score):
        places = []
        for place in self.restaurants.keys():
            if int(self.restaurants[place]['fave']) == score:
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
            restaurants = self.add_restaurant(restaurants)
        elif choice == "4":
            self.save_changes_as_json(self.filename)
        elif choice == "5":
            self.finished = True
        else:
            print "That's not a valid choice - try again!"
    
    
    def search_on_distance(self,dist):
        """Prints out all restaurants within a given distance"""
        for restaurant_name in self.restaurants.keys():
            rest_details = self.restaurants[restaurant_name]
            if int(rest_details["dist"]) <= int(dist):
                print restaurant_name + " is a " + rest_details["type"] + " place " + \
                rest_details["dist"] + " minutes from here"
        

    def search_on_rating(self,rating):
        """Prints out all restaurants with a given rating or better"""
        for restaurant_name in restaurants.keys():
            rest_details = restaurants[restaurant_name]
            if int(rest_details["fave"]) >= int(rating):
                print restaurant_name + " is a " + rest_details["fave"] + "/5 rated place " + \
                str(rest_details["dist"]) + " minutes from here"


    def add_restaurant(self):
        """Prompts the user for a new restaurant to add to the database"""
        name = raw_input("Enter Restaurant Name: ")
        cuisine = raw_input("Enter Restaurant type: ")
        cost = raw_input("Enter Restaurant cost (out of 5): ")
        fave = raw_input("Enter cost (out of 5): ")
        dist = raw_input("Enter distance (minutes' walk): ")
        restaurants[name] = {"type": cuisine, "cost": cost, 
                            "fave": fave, "dist": dist}


    def save_changes(self,filename):
        """Saves the current restaurant list to a CSV file"""
        with open(filename,"w") as csvfile:
            csv_writer = csv.DictWriter(csvfile, fieldnames=['name', 'type', 'cost', 'fave', 'dist'])
            csv_writer.writeheader()
            for restaurant_name in restaurants.keys():
                rest_details = self.restaurants[restaurant_name]
                rest_details['name'] = restaurant_name
                csv_writer.writerow(rest_details) 

    def read_csvfile(self,filename):
        """Reads the restaurant list from a CSV file"""
        with open(filename) as csvfile:
            csv_reader = csv.DictReader(csvfile)
            for rest_details in csv_reader: 
                restaurant_name = rest_details['name']
                del rest_details['name']
                self.restaurants[restaurant_name] = rest_details
                
    def save_changes_as_json(self, filename):
        """Saves the restaurant data as JSON"""
        filename = filename.replace('csv','json')
        with open(filename, 'w') as jsonfile:
            json.dump(self.restaurants, jsonfile, sort_keys=True,
                      indent=2, separators=(',',':'))

    def read_jsonfile(self, filename):
        """Saves the restaurant data as JSON"""
        filename = filename.replace('csv','json')
        with open(filename, 'r') as jsonfile:
            self.restaurants = json.load(jsonfile)

            