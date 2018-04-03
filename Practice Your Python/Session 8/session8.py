valid_routes = {
    "ALC": ["CDG", "LHR", "LGW"],  # Planes depart ALC for CDG, LHR and LGW airports
    "LHR": [],
    "LGW": ["ALC", "LED", "CDG"],
    "LED": ["MAN", "ALC"],
    "MAN": ["CDG"],
    "CDG": ["MAN", "LGW"],
    "LRX": ["LGW", "ALC"],
    "STD": ["YYZ"],
    "YYZ": ["STD"],
    "SEA": ["LRX"]

}


def reachable_destination(origin, destination):
    return None
