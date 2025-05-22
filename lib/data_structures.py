spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    string_spicy_foods = [spicy_foods[i]['name'] for i in range(len(spicy_foods))]
    return string_spicy_foods

def get_spiciest_foods(spicy_foods):
    spiciest_foods = [spicy_foods[i] for i in range(len(spicy_foods)) if spicy_foods[i]['heat_level'] > 5]
    return spiciest_foods

def print_spicy_foods(spicy_foods):
    [print(f"{spicy_foods[i]['name']} ({spicy_foods[i]['cuisine']}) | Heat Level: {'🌶' * spicy_foods[i]['heat_level']}") for i in range(len(spicy_foods))]

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    match = [spicy_foods[i] for i in range(len(spicy_foods)) if spicy_foods[i]['cuisine'] == cuisine]
    return match[0] if match else None

def print_spiciest_foods(spicy_foods):
    [print(f"{spicy_foods[i]['name']} ({spicy_foods[i]['cuisine']}) | Heat Level: {'🌶' * spicy_foods[i]['heat_level']}") for i in range(len(spicy_foods)) if spicy_foods[i]['heat_level'] > 5]

def get_average_heat_level(spicy_foods):
    total_heat_level = sum([spicy_foods[i]['heat_level'] for i in range(len(spicy_foods))])
    average_heat_level = total_heat_level / len(spicy_foods)
    return average_heat_level

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
