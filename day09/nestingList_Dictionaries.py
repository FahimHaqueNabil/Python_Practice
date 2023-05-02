# Nesting List in a Dictionary

travel_log = {
    "France": ["Paris", "Leon", "Dijon"],
    "Germany": ["Frankfurt", "Berlin", "Hamburg"],
}


# Nesting Dictionary in a Dictionary

travel_log2 = {
    "France": {"cities_visited": ["Paris", "Leon", "Dijon"], "total_visits": 12},
    "Germany": {"cities_visited": ["Frankfurt", "Berlin", "Hamburg"], "total_visits": 5},
}

# Nesting  Dictionary in a List

travel_log3 = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Leon", "Dijon"],
        "total_visits": 12
    },
    {
        "country": "Germany",
        "cities_visited": ["Frankfurt", "Berlin", "Hamburg"],
        "total_visits": 5
    },
]

def add_new_country(country_visited, cities, visits):
    new_country = {}
    new_country["country"] = country_visited
    new_country["cities_visited"] = cities
    new_country["total_visits"] = visits
    travel_log3.append(new_country)

add_new_country("Russia", ["Moscow", "Saint Petersburg"], 2)
print(travel_log3)