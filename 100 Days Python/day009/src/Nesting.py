# Nesting 
capitals = {
    "France": "Paris",
    "India": "New Delhi",
    "Japan": "Tokyo",
    "Germany": "Berlin",
}

# Nesting a List in a Dictionary
travel_log = {
    "India": ["New Delhi", "Mumbai", "Kolkata", "Dehradun", "Amritsar"],
    "Germany": ["Berlin", "Munich", "Hamburg"],
}

# Nesting a Dictionary in a Dictionary
travel_log = {
    "India": {"cities_visited": ["New Delhi", "Mumbai", "Kolkata", "Dehradun", "Amritsar"], "total_visits": 12},
    "Germany": {"cities_visited": ["Berlin", "Munich", "Hamburg"], "total_visits": 8},
}

# Nesting a Dictionary in a List
travel_log = [
    {
        "country": "India", 
        "cities_visited": ["New Delhi", "Mumbai", "Kolkata", "Dehradun", "Amritsar"], 
        "total_visits": 12,
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Munich", "Hamburg"], 
        "total_visits": 8,
    },
]
