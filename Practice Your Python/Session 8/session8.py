def reachable_destination(origin, destination):
    valid_routes = {
        "ALC": ["CDG", "LHR", "LGW", "JFK"],  # Planes depart ALC for CDG, LHR, LGW and JFK airports
        "CDG": ["MAN", "LGW"],
        "JFK": ["SEA"],
        "LED": ["MAN", "ALC"],
        "LGW": ["ALC", "LED", "CDG"],
        "LHR": [],
        "LC7": ["LGW", "ALC"],
        "MAN": ["CDG"],
        "SEA": ["LC7"],
        "STD": ["YYZ"],
        "YYZ": ["STD"]
    }

    return None