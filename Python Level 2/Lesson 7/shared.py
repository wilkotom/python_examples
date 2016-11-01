import csv


def return_verified_value(min, max, value):
    """Returns an integer between two values.
    Arguments in order: min, max, value to check"""
    verified_value = None
    while verified_value is None:
        try:
            verified_value = int(value)
            if verified_value < min or verified_value > max:
                verified_value = None
        except ValueError:
            verified_value = None
        if verified_value is None:
            value = raw_input('Please enter a value between {0} and {1}'.format(min, max))
    return value


def save_changes(filename, restaurants):
    with open(filename, "w") as csvfile:
        csv_writer = csv.DictWriter(csvfile, fieldnames=['name', 'type', 'cost', 'fave', 'dist'])
        csv_writer.writeheader()
        for name in restaurants.keys():
            csv_writer.writerow(restaurants[name].as_dict())


def read_csvfile(filename):
    restaurants = {}
    with open(filename) as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for rest_details in csv_reader:
            restaurants[rest_details['name']] = Restaurant(**rest_details)
            # Because the column headers match the Restaurant properties' names, we can use **rest_details as shorthand
            # We could alo write this as:
            # Restaurant(rest_details['name'],
            #            rest_details['type'],
            #            rest_details['cost'],
            #            rest_details['fave'],
            #            rest_details['dist'])
    return restaurants



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

    def as_dict(self):
        return {'type': self.type,
                'cost': self.cost,
                'fave': self.fave,
                'dist': self.dist,
                'name': self}


class Formal(Restaurant):
    """Restaurants which require a reservation and have a dress code"""
    def make_reservation(self):
        print "In the future we'll implement this function."
        print "It'll attempt to make a reservation at {0}".format(self.name)


class FastCasual(Restaurant):
    """Restaurants which don't accept reservations"""
    def request_delivery(self):
        print "In the future we'll implement this function."
        print "It'll request delivery from {0}".format(self.name)

