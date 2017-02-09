import csv

def return_verified_value(min,max,value):
    """Returns an integer between two values.
    Arguments in order: min, max, value to check"""
    verified = False
    while verified is False:
        try:
            if int(value) >= min and int(value) <= max:
                verified = True
        except ValueError:
            pass
        if verified is False:
            value = raw_input("Please enter a number between {0} and {1}:".format(min,max))
    return value  #


def save_changes(restaurants):
    with open("restaurants-lesson2.csv","w") as csvfile:
        csv_writer = csv.DictWriter(csvfile, fieldnames=['name', 'type', 'cost', 'fave', 'dist'])
        csv_writer.writeheader()
        for restaurant_name in restaurants.keys():
            rest_object = restaurants[restaurant_name]
            #  This code needs to be updated to pull the data from a Restaurant
            #  object instead of a dictionary eg using rest_object.name, rest_object.type, etc
            rest_object['name'] = restaurant_name  
            csv_writer.writerow(rest_object)


def read_csvfile(restaurants):
    with open("restaurants-lesson2.csv") as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for rest_details in csv_reader:
            restaurants[rest_details['name']] = Restaurant(rest_details['name'],
                                                           rest_details['type'],
                                                           rest_details['cost'],
                                                           rest_details['fave'],
                                                           rest_details['dist'])


class Restaurant:
    """Holds details of an individual place to eat"""
    def __init__(self, name, type, cost, fave, dist):
        self.name = name
        self.type = type
        self.cost = int(cost)  # This (and following lines) ensure that these values are numbers
        self.fave = int(fave)  # If you have some extra time you might like to add better input validation here
        self.dist = int(dist)  # What will happen if we create a Restaurant with a non-number in these fields?

    def __str__(self):
        return "{0} is a {1} place {4} minutes from here. Star rating {2}, Cost {3}".format(
            self.name, self.type, self.cost, self.fave, self.dist)