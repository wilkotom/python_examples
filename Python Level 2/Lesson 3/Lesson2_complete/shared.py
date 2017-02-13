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
            rest_object['name'] = restaurant_name
            csv_writer.writerow(rest_object)


def read_csvfile(restaurants):
    with open("restaurants-lesson2.csv") as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for rest_details in csv_reader:
            restaurants[rest_details['name']] = {'type': rest_details['type'],
                                                 'cost': rest_details['cost'],
                                                 'fave': rest_details['fave'],
                                                 'dist': rest_details['dist']}
